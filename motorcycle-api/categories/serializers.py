from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'pilots_amount', 'motorization', 'last_champion']  # noqa:E501

    def validate_name(self, value):
        return value

    def validate_pilots_amount(self, value):
        return value

    def validate_motorization(self, value):
        return value

    def validate_last_champion(self, value):
        return value
