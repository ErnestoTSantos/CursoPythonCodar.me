import re
from datetime import datetime, timedelta

from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils import timezone
from rest_framework import serializers

from schedule.models import Scheduling


class SchedulingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scheduling
        fields = ['id', 'date_time', 'client_name', 'client_email', 'client_phone']  # noqa:E501

    def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError('O agendamento não pode ser realizado no passado!')  # noqa:E501
        return value

    def validate(self, attrs):
        date_time = attrs.get('date_time', '')
        client_name = attrs.get('client_name', '')
        client_email = attrs.get('client_email', '')
        client_phone = attrs.get('client_phone', '')

        verification_numbers = re.sub(r'[^0-9+() -]', '', client_phone)

        amount_caracters_phone = len(client_phone)

        amount_caracters_name = len(client_name)

        obj = None
        qs = None

        if date_time and datetime.date(date_time).weekday() == 6:
            raise serializers.ValidationError('Infelizmente o estabelecimento não trabalha aos domingos!')  # noqa:E501

        if date_time:
            time = datetime.strftime(date_time, '%H:%M')

            lunch_time = datetime(2022, 5, 15, 12, 00)
            lunch_time = datetime.strftime(lunch_time, '%H:%M')

            return_interval = datetime(2022, 5, 15, 13, 00)
            return_interval = datetime.strftime(return_interval, '%H:%M')

            open_time = datetime(2022, 5, 15, 9, 0)
            open_time = datetime.strftime(open_time, '%H:%M')

            closing_time = datetime(2022, 5, 15, 18, 00)
            closing_time = datetime.strftime(closing_time, '%H:%M')

            if datetime.date(date_time).weekday() == 5 and time > return_interval:  # noqa:E501
                raise serializers.ValidationError('Infelizmente o estabelecimento só trabalha até as 13h no sábado!')  # noqa:E501
            elif return_interval > time >= lunch_time:
                raise serializers.ValidationError('Os funcionários estão no horário de almoço!')  # noqa:E501
            elif open_time > time:
                raise serializers.ValidationError('O estabelecimento abre apenas às 9h!')  # noqa:E501
            elif closing_time <= time:
                raise serializers.ValidationError('O estabelecimento fehca às 18h!')  # noqa:E501

        try:
            obj = get_object_or_404(Scheduling, client_email=client_email, canceled=False, date_time__date=date_time)  # noqa:E501
        except Http404:
            pass

        try:
            qs = get_list_or_404(Scheduling, canceled=False)  # noqa:E501
        except Http404:
            pass

        if client_name and amount_caracters_name < 3:
            raise serializers.ValidationError('O nome do cliente precisa ter 3 ou mais caracteres!')  # noqa:E501

        if client_email.endswith('.br') and client_phone.startswith('+') and not client_phone.startswith('+55'):  # noqa:E501
            raise serializers.ValidationError('E-mail brasileiro deve estar associado a um número do Brasil (+55)')  # noqa:E501

        if client_phone and amount_caracters_phone < 8:
            raise serializers.ValidationError('O número de telefone precisa ter no mínimo 8 digitos!')  # noqa:E501

        if client_phone != verification_numbers:
            raise serializers.ValidationError('O número pode ter apenas valores entre 0-9, parenteses, traços, espaço e o sinal de mais!')  # noqa:E501

        if obj:
            raise serializers.ValidationError(f'O(A) cliente {obj.client_name} não pode fazer duas reservas no mesmo dia')  # noqa:E501

        if date_time:
            for element in qs:
                date_element = datetime.date(element.date_time)
                date_request = datetime.date(date_time)

                if date_element == date_request:
                    if element.date_time + timedelta(minutes=30) <= date_time and date_time + timedelta(minutes=30) <= element.date_time:  # noqa:E501
                        pass
                    else:
                        raise serializers.ValidationError('Infelizmente o horário selecionado está inválido no momento!')  # noqa:E501

        return attrs
