"""

a. Módulo usuario.py
    I. Deve conter uma classe Usuario
    II. Classe Usuario deve ter um construtor que recebe nome e email
    III. Classe Usuario deve possuir um método de instância imprime_usuario que
    imprime: "Gabriel (gabriel@exemplo.com)", para uma instância com nome =
    "Gabriel" e email = "gabriel@exemplo.com"
    IV. Classe Usuario deve possuir um atributo de classe quantidade que
    armazena a quantidade de instâncias criadas, sejam instâncias de Usuario
    ou de qualquer classe que estenda Usuario . Por exemplo:
    Administrador(Usuario).

"""


class User:
    user_id = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.user_id += 1
        self.user_id = User.user_id

    def print_user_details(self):
        print(f'{self.name} ({self.email})')
        print('-' * 30)

    def print_user_id(self):
        print(f'O id do usuário {self.name} é: \033[32m{self.user_id}\033[m')
