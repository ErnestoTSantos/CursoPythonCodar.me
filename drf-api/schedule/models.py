from django.db import models


class Scheduling(models.Model):
    ACTION_STATES = [
        ('NCNF', 'Not confirmed'),
        ('CONF', 'Confirmed'),
        ('EXEC', 'Executed'),
        ('CANC', 'Canceled')
    ]

    provider = models.ForeignKey('auth.User', related_name='scheduling', on_delete=models.CASCADE, verbose_name='Prestador do serviço')  # noqa:E501
    date_time = models.DateTimeField('Data e hora')
    client_name = models.CharField('Nome do cliente', max_length=200)
    client_email = models.EmailField('E-mail do cliente')
    client_phone = models.CharField('Número do cliente', max_length=20)
    states = models.CharField('Estados do elemento', max_length=4, choices=ACTION_STATES, default='NCNF')  # noqa:E501
    confirmed = models.BooleanField('Horário confirmado', default=False)
    canceled = models.BooleanField('Horário cancelado', default=False)

    def __str__(self):
        return self.client_name


class Faithfulness(models.Model):
    provider = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='faithfulness', verbose_name='Prestador do serviço')  # noqa:E501
    client = models.CharField('Nome do cliente', max_length=200, unique=True)
    level = models.IntegerField('Fidelidade', default=0)

    def __str__(self):
        return f'{self.client} = {self.level}'
