from categories.models import Category
from django.db import models


class Pilot(models.Model):
    name = models.CharField('Nome do piloto', max_length=50, unique=True)
    age = models.IntegerField('Idade')
    number = models.IntegerField('Número do piloto', unique=True)
    automaker = models.CharField('Montadora', max_length=50)
    championships_won = models.IntegerField('Campeonatos vencidos')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)  # noqa:E501
    retired = models.BooleanField('Está aposentado', default=False)  # noqa:E501

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pilot'
        verbose_name_plural = 'Pilots'
