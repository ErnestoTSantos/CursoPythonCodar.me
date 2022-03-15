from rest_framework import serializers

from schedule.models import Scheduling


class SchedulingSerializer(serializers.Serializer):
    date_time = serializers.DateTimeField()
    client_name = serializers.CharField(max_length=200)
    client_email = serializers.EmailField()
    client_phone = serializers.CharField(max_length=20)

    def create(self, validated_data):
        # Como um agendamento será criado.
        scheduling = Scheduling.objects.create(
            date_time=validated_data['date_time'],
            client_name=validated_data['client_name'],
            client_email=validated_data['client_email'],
            client_phone=validated_data['client_phone'],
        )
        return scheduling

    def update(self, instance, validated_data):
        instance.date_time = validated_data.get('date_time', instance.date_time)  # noqa:E501
        instance.client_name = validated_data.get('client_name', instance.client_name)  # noqa:E501
        instance.client_email = validated_data.get('client_email', instance.client_email)  # noqa:E501
        instance.client_phone = validated_data.get('client_phone', instance.client_phone)  # noqa:E501
        instance.save()
        return instance
