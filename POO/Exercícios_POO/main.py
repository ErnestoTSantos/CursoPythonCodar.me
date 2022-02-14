from admin import Admin
from users import User

user = User("Gabriel", "gabriel@exemplo.com")
admin = Admin("Admin", "admin@exemplo.com")
# => "Gabriel (gabriel@exemplo.com)
user.print_user_details()
# => "Admin (admin@exemplo.com) – Administrador"
admin.print_user_details()
print(User.user_id)
# => 2
