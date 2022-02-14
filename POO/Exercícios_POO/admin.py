from users import User


class Admin(User):

    def __init__(self, name, email):
        super().__init__(name, email)

    def print_user_details(self):
        print(f'{self.name} ({self.email}) – Administrador')
        print('-' * 30)
