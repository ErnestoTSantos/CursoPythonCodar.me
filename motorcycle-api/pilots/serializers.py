from categories.models import Category
from rest_framework import serializers

from .models import Pilot


class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = ['id', 'name', 'age', 'number', 'automaker', 'championships_won', 'category']  # noqa:E501

    category = serializers.CharField()

    def validate_name(self, value):
        amount_characters = len(value)

        if amount_characters < 6:
            raise serializers.ValidationError('O nome precisa ter mais de 10 caracteres!')  # noqa:E501

        if ' ' not in value:
            raise serializers.ValidationError('O nome precisa ser composto por um sobrenome!')  # noqa:E501

        return value

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError('O piloto precisa ter uma idade igual ou superior a 18 anos!')   # noqa:E501

        return value

    def validate_number(self, value):
        if value > 200:
            raise serializers.ValidationError('O número do piloto precisa ser menor que 200!')  # noqa:E501

        return value

    def validate_automaker(self, value):
        qs = Pilot.objects.filter(automaker=value, retired=False)

        count_automakers = qs.count()

        if count_automakers > 1:
            raise serializers.ValidationError('Infelizmente a montadora só pode ter dois pilotos por temporada!')   # noqa:E501

        return value

    def validate_championships_won(self, value):
        if value < 0:
            raise serializers.ValidationError('A quantidade de títulos precisa ser igual ou superior a 0!')  # noqa:E501

        return value

    def validate_category(self, value):
        obj = Category.objects.filter(name=value).first()

        if not obj:
            raise serializers.ValidationError('Infelizmente a categoria enviada não existe!')  # noqa:E501

        return obj
