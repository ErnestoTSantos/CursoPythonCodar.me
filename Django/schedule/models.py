from django.db import models


class Category(models.Model):
    name = models.CharField('Nome da classe', max_length=255, unique=True)
    description = models.TextField(
        'Descrição', null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def create_class(cls, name, description=None):

        if not name:
            raise ValueError('A categoria precisa de um nome!')

        if name and description:
            category = Category(name=name, description=description)
        else:
            category = Category(name=name,)

        category.save()

        return category


class Event(models.Model):
    name = models.CharField('Nome', max_length=255)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    place = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    date = models.DateField(null=True)
    participants = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def create_event(cls, name, category, place=None, link=None, date=None):

        if not name:
            raise ValueError('O evento precisa ter um nome!')

        if not category:
            raise ValueError('O evento precisa ter uma categoria!')

        if place and link:
            raise ValueError('O evento não pode ter um local e um link. Precisa ter apenas um dos dois!')  # noqa:E501

        if place and date:
            event = Event(name=name, category=category, place=place, date=date)
        elif link and date:
            event = Event(name=name, category=category, link=link, date=date)
        elif place:
            event = Event(name=name, category=category, place=place)
        elif link:
            event = Event(name=name, category=category, link=link)
        else:
            event = Event(name=name, category=category,)

        event.save()

        return event
