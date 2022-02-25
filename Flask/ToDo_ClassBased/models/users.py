from random import choice, randint

from models.ToDo import ToDo


class Users:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}'


chores_list = ['Melhorar Django', 'Aprender Flask',
               'Melhorar conceitos Python', 'Aprender Express', 'Aprender Javascript']  # noqa:E501
dates = ['26/02/2022', '30/04/2025', '21/03/2022',
         '24/07/2022', '10/03/2022', '28/04/2022']

names = ['Ernesto Silva', 'João Machado', 'Maria Santos', 'Júlia Henz',
         'Luisa Oliveira', 'Carla Lemes', 'Gabriel Oliveira', 'Carlos Santos',
         'Mateus Henz', 'Juliana Lemes']


users = []

chores = []

for i in range(0, 6):
    name = choice(names)
    age = randint(18, 40)

    users.append(Users(name, age))

for j in range(0, 10):
    user = choice(users)
    chore = choice(chores_list)
    date = choice(dates)

    chores.append(ToDo(user, chore, date))
