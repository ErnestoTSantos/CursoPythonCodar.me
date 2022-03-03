from django.db import models


class Author(models.Model):
    first_name = models.CharField('Primeiro nome', max_length=20)
    last_name = models.CharField('Sobrenome', max_length=40, blank=True)
    age = models.IntegerField('Idade')

    def __str__(self):
        return f'{self.first_name}'

    @classmethod
    def create_author(cls, first_name, age, last_name=''):

        if not first_name:
            raise ValueError('O autor precisa ter um primeiro nome!')

        if not age:
            raise ValueError('O autor precisa ter uma idade!')

        if last_name:
            author = Author(first_name=first_name,
                            last_name=last_name, age=age)
        else:
            author = Author(first_name=first_name, age=age)

        author.save()

        return author
