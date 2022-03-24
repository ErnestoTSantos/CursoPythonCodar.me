import re
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers

from schedule.models import Scheduling


class SchedulingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scheduling
        fields = ['id', 'provider', 'date_time', 'client_name', 'client_email', 'client_phone', 'confirmed', 'states']  # noqa:E501

    provider = serializers.CharField()

    def get_hour(self, value, hour, minutes):
        date = datetime(value.year, value.month, value.day, hour, minutes)
        return date.strftime('%H:%M')

    def validate_provider(self, value):
        try:
            provider_obj = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError('Username não existe!')

        # Podemos retornar apenas o objeto,
        # pois o django por baixo dos panos sabe resolver qual será o objeto.
        return provider_obj

    def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError('O agendamento não pode ser realizado no passado!')  # noqa:E501

        if value and datetime.date(value).weekday() == 6:
            raise serializers.ValidationError('Infelizmente o estabelecimento não trabalha aos domingos!')  # noqa:E501

        if value:
            time = datetime.strftime(value, '%H:%M')

            lunch_time = self.get_hour(value, 12, 0)

            return_interval = self.get_hour(value, 13, 0)

            open_time = self.get_hour(value, 9, 0)

            closing_time = self.get_hour(value, 18, 0)

            if datetime.date(value).weekday() == 5 and time >= return_interval:  # noqa:E501
                raise serializers.ValidationError('Infelizmente o estabelecimento só trabalha até as 13h no sábado!')  # noqa:E501
            elif return_interval > time >= lunch_time and datetime.date(value).weekday() != 5:  # noqa:E501
                raise serializers.ValidationError('Os funcionários estão no horário de almoço!')  # noqa:E501
            elif open_time > time:
                raise serializers.ValidationError('O estabelecimento abre apenas às 9h!')  # noqa:E501
            elif closing_time <= time:
                raise serializers.ValidationError('O estabelecimento fehca às 18h!')  # noqa:E501

        qs = Scheduling.objects.filter(canceled=False, confirmed=True)  # noqa:E501

        delta = timedelta(minutes=30)

        if qs:
            for element in qs:
                date_element = datetime.date(element.date_time)
                date_request = datetime.date(value)

                if date_element == date_request:
                    if element.date_time + delta <= value or value + delta <= element.date_time:  # noqa:E501
                        pass
                    else:
                        raise serializers.ValidationError('Infelizmente o horário selecionado está indisponível!')  # noqa:E501

        return value

    def validate_client_name(self, value):
        amount_characters_name = len(value)

        if amount_characters_name < 7:
            raise serializers.ValidationError('O nome do cliente precisa ter 7 ou mais caracteres!')  # noqa:E501

        return value

    def validate_client_phone(self, value):
        verification_numbers = re.sub(r'[^0-9+() -]', '', value)
        amount_characters_phone = len(value)

        if value and amount_characters_phone < 8:
            raise serializers.ValidationError('O número de telefone precisa ter no mínimo 8 digitos!')  # noqa:E501

        if value != verification_numbers:
            raise serializers.ValidationError('O número pode ter apenas valores entre 0-9, parenteses, traços, espaço e o sinal de mais!')  # noqa:E501

        return value

    def validate_state(self, value):
        print(value)

    def validate(self, attrs):
        provider = attrs.get('provider', '')
        date_time = attrs.get('date_time', '')
        client_email = attrs.get('client_email', '')
        client_phone = attrs.get('client_phone', '')

        if date_time and client_email:
            if Scheduling.objects.filter(provider__username=provider, client_email=client_email, canceled=False, date_time__date=date_time).exists():  # noqa:E501
                raise serializers.ValidationError('O(A) cliente não pode ter duas reservas no mesmo dia!')  # noqa:E501

        if client_email.endswith('.br') and client_phone.startswith('+') and not client_phone.startswith('+55'):  # noqa:E501
            raise serializers.ValidationError('E-mail brasileiro deve estar associado a um número do Brasil (+55)')  # noqa:E501

        return attrs


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'scheduling']

    scheduling = SchedulingSerializer(many=True, read_only=True)
