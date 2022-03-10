from django.db import models


class Category(models.Model):
    name = models.CharField('Nome da classe', max_length=255, unique=True)
    description = models.TextField(
        'Descrição', null=True, blank=True, max_length=100)
    active = models.BooleanField('Ativa', default=True)

    def __str__(self):
        return self.name

    @classmethod
    def create_class(cls, name, description=None, active=True):

        if not name:
            raise ValueError('A categoria precisa de um nome!')

        if active != True and active != False:
            raise ValueError('A categoria precisa ser ativa ou não!')

        if name and description:
            category = Category(
                name=name, description=description, active=active)
        else:
            category = Category(name=name, active=active)

        category.save()

        return category


class Event(models.Model):
    name = models.CharField('Nome', max_length=255)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    place = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    date = models.DateField('Data do evento', null=True, blank=True)
    participants = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def create_event(cls, name, category, date=None, place=None, link=None):

        if not name:
            raise ValueError('O evento precisa ter um nome!')

        if not category:
            raise ValueError('O evento precisa ter uma categoria!')

        if place and link:
            raise ValueError('O evento não pode ter um local e um link. Precisa ter apenas um dos dois!')  # noqa:E501

        if place:
            event = Event(name=name, category=category, place=place, date=date)
        elif link:
            event = Event(name=name, category=category, link=link, date=date)
        else:
            event = Event(name=name, category=category, date=date)

        event.save()

        return event
