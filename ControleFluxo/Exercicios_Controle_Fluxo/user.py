user_static = 'Astrin'
password_static = '123456'

user_name = input('Digite o nome de usuário: ')
user_password = input('Digite a senha do usuário: ')

if user_static != user_name and password_static != user_password:
    print('Usuário e senha incompatível!')
elif user_static != user_name:
    print('Usuário incompatível!')
elif password_static != user_password:
    print('Senha incompatível!')
if user_static == user_name and password_static == user_password:
    print(f'Seja bem vindo {user_static}')
