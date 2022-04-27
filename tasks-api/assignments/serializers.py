from datetime import date

from django.contrib.auth.models import User
from rest_framework import serializers

from assignments.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = [
            "id",
            "creator",
            "task_name",
            "description",
            "create_day",
            "final_day",
            "active",
        ]

    creator = serializers.CharField(max_length=50)

    def validate_creator(self, value):
        obj = User.objects.filter(username=value)

        if not obj.exists():
            raise serializers.ValidationError("O criador informado não existe!")

        return obj.first()

    def validate_task_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "O nome da tarefa precisa ter 5 ou mais caracteres!"
            )

        return value

    def validate_final_day(self, value):
        if value < date.today():
            raise serializers.ValidationError(
                "A finalização não pode ser realizada no passado!"
            )

        return value

    def validate(self, attrs):
        return attrs
