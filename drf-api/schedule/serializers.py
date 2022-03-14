from rest_framework import serializers


class SchedulingSerializer(serializers.Serializer):
    date_time = serializers.DateTimeField()
    client_name = serializers.CharField(max_length=200)
    client_email = serializers.EmailField()
    client_phone = serializers.CharField(max_length=20)
