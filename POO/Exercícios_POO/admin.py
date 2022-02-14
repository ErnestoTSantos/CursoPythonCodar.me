"""

b. Módulo administrador.py
    I. Deve conter uma classe Administrador que estende (herda de) Usuario .
    II. Deve sobrescrever o método imprime_usuario e imprimir: "Gabriel
    (gabriel@exemplo.com) – Administrador", para uma instância com nome =
    "Gabriel" e email = "gabriel@exemplo.com”

"""

from users import User


class Admin(User):

    def __init__(self, name, email):
        super().__init__(name, email)

    def print_user_details(self):
        print(f'{self.name} ({self.email}) – Administrador')
        print('-' * 30)
