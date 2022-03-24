from django.db import models


class Scheduling(models.Model):
    provider = models.ForeignKey('auth.User', related_name='scheduling', on_delete=models.CASCADE, verbose_name='Prestador do serviço')  # noqa:E501
    date_time = models.DateTimeField('Data e hora')
    client_name = models.CharField('Nome do cliente', max_length=200)
    client_email = models.EmailField('E-mail do cliente')
    client_phone = models.CharField('Número do cliente', max_length=20)
    canceled = models.BooleanField('Horário cancelado', default=False)

    def __str__(self):
        return self.client_name
