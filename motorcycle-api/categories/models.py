from django.db import models


class Category(models.Model):
    name = models.CharField('Nome da categoria', max_length=50)
    pilots_amount = models.IntegerField('Número máximo de pilotos')
    motorization = models.IntegerField('Potência do motor')
    last_champion = models.CharField('Nome do último campeão', max_length=50)
    active = models.BooleanField('Categoria ativa', default=True)

    def __str__(self):
        return self.name
