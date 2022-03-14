from datetime import datetime

from accommodations.models import Accommodation
from django.db import models
from django.shortcuts import get_list_or_404, get_object_or_404


class Reserve(models.Model):
    accommodation = models.ForeignKey(Accommodation, verbose_name='Acomodação', on_delete=models.CASCADE)  # noqa:E501
    check_in = models.DateField('Data do check-in')
    check_out = models.DateField('Data do check-out')
    person = models.CharField('Nome da reserva', max_length=50)
    amount_people = models.IntegerField('Número de pessoas')

    def __str__(self):
        return f'{self.accommodation.accommodation_name}, {self.person}'

    @classmethod
    def create_reservation(cls, accommodation, check_in, check_out, person, amount_people):  # noqa:E501
        check_in = datetime.strptime(check_in, '%Y-%m-%d').date()
        check_out = datetime.strptime(check_out, '%Y-%m-%d').date()

        if not accommodation:
            raise ValueError('A reserva precisa de uma acomodação!')

        if not check_in:
            raise ValueError('A reserva precisa ter uma data de entrada!')

        if not check_out:
            raise ValueError('A reserva precisa ter uma data de saída!')

        if not person:
            raise ValueError('É necessário passar um nome com sobrenome para reservar!')  # noqa:E501

        if not amount_people:
            raise ValueError('É necessário passar o número de pessoas!')

        reserve_comparation = get_list_or_404(Reserve, accommodation=accommodation)  # noqa:E501

        verification = False
        for reserve in reserve_comparation:
            if check_in > reserve.check_in < check_out and check_in >= reserve.check_out < check_out or reserve.check_in >= check_out < reserve.check_out and reserve.check_in > check_in <= reserve.check_out:  # noqa:E501
                verification = True

        if verification:
            reserve = Reserve(accommodation=accommodation, check_in=check_in, check_out=check_out, person=person, amount_people=amount_people)  # noqa:E501

            accommodation.times_rented += 1

            accommodation.save()

            reserve.save()

            return reserve
        else:
            raise ValueError(
                'Infelizmente o quarto já está ocupado durante esse período!')
