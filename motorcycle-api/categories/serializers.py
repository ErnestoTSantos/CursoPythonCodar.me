from pilots.serializers import PilotSerializer
from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'pilots_amount', 'motorization', 'last_champion']  # noqa:E501

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError(f'A categoria {value} já existe!')  # noqa:E501

        if len(value) < 5:
            raise serializers.ValidationError('A categoria precisa ter mais de 4 caracteres!')  # noqa:E501

        return value

    def validate_pilots_amount(self, value):
        if value < 10:
            raise serializers.ValidationError('A categoria precisa poder ter mais de 10 pilotos!')  # noqa:E501

        return value

    def validate_motorization(self, value):
        if value < 125:
            raise serializers.ValidationError('A categoria precisa ter mais de 124cc!')  # noqa:E501

        return value

    def validate_last_champion(self, value):
        if ' ' not in value:
            raise serializers.ValidationError('O nome do último campeão precisa ser composto de nome e sobrenome!')  # noqa:E501

        if len(value) < 6:
            raise serializers.ValidationError('O nome do último campeão precisa ter mais de 5 caracteres!')  # noqa:E501

        return value


class CategoryPilotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'pilots_amount',
                  'motorization', 'last_champion', 'pilots']

    pilots = PilotSerializer(many=True, read_only=True)
