import re
from datetime import datetime, timedelta
from xml.dom import NotFoundErr

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

        obj = None
        qs = None

        if date_time and client_phone and client_email and client_name:
            try:
                obj = get_object_or_404(Scheduling, client_email=client_email, canceled=False)  # noqa:E501
            except NotFoundErr:
                pass
        try:
            qs = get_list_or_404(Scheduling, canceled=False)  # noqa:E501
        except NotFoundErr:
            pass

        if client_email.endswith('.br') and client_phone.startswith('+') and not client_phone.startswith('+55'):  # noqa:E501
            raise serializers.ValidationError('E-mail brasileiro deve estar associado a um número do Brasil (+55)')  # noqa:E501

        if amount_caracters_phone < 8:
            raise serializers.ValidationError('O número de telefone precisa ter no mínimo 8 digitos!')  # noqa:E501

        if client_phone != verification_numbers:
            raise serializers.ValidationError('O número pode ter apenas valores entre 0-9, parenteses, traços, espaço e o sinal de mais!')  # noqa:E501

        if obj:
            if datetime.date(obj.date_time) == datetime.date(date_time):
                raise serializers.ValidationError(f'O cliente {obj.client_name} não pode fazer duas reservas no mesmo dia')  # noqa:E501

        if date_time:
            for element in qs:
                date_element = datetime.date(element.date_time)
                date_request = datetime.date(date_time)

                if date_element == date_request:
                    if element.date_time + timedelta(minutes=30) <= date_time:  # noqa:E501
                        pass
                    elif date_time + timedelta(minutes=30) <= element.date_time:
                        pass
                    else:
                        raise serializers.ValidationError('Infelizmente o horário selecionado está inválido no momento!')  # noqa:E501

        return attrs
