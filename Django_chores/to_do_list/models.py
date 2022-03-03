from django.db import models


class Chore(models.Model):
    author = models.ForeignKey(
        'authors.Author', on_delete=models.DO_NOTHING, verbose_name='Autor')
    name = models.CharField('Nome da tarefa', max_length=50)
    active = models.BooleanField('Ativo', default=True)
    create_date = models.DateField('Data da criação', auto_now_add=True)
    update_date = models.DateField('Data de atualização', auto_now=True)
    final_date = models.DateField('Data de finalização', blank=True, null=True)

    def __str__(self):
        return f'Author: {self.author}, Task: {self.name}'

    @classmethod
    def create_chore(cls, author, name, active=True, final_date=''):

        if not author:
            raise ValueError('Sua tarefa precisa ter um autor!')

        if not name:
            raise ValueError('Sua tarefa precisa ter um nome!')

        if not active and final_date:
            chore = Chore(author=author, name=name,
                          active=active, final_date=final_date)
        elif final_date:
            chore = Chore(author=author, name=name,
                          active=active, final_date=final_date)
        else:
            chore = Chore(author=author, name=name, active=active)

        chore.save()

        return chore
