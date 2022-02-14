"""

c. Módulo main.py `
    a. Deve importar os módulos usuario.py e administrador.py .
    b. Deve ser executado contendo as instruções abaixo:
        user => "Gabriel (gabriel@exemplo.com)
        admin => "Admin (admin@exemplo.com) – Administrador"
        User.user_id => 2

"""

from admin import Admin
from users import User

user = User("Gabriel", "gabriel@exemplo.com")
admin = Admin("Admin", "admin@exemplo.com")

user.print_user_details()
admin.print_user_details()
print(User.user_id)
