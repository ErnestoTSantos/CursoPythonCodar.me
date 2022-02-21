import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from users import Users

"""

Tendo como base o arquivo base_server.py e o template HTML
listar_usuarios.html, implemente um servidor utilizando a
classe HTTPServer do Python nas seguintes especificações:

O servidor deve possuir uma lista de Usuários
Toda instância de Usuário deve possuir os atributos:
    id (int)
    nome (str)
    email (str)
    senha (str)
O atributo id deve ser auto-incrementado para cada novo usuário criado.
O servidor deve possuir uma rota /usuarios/ que lista os usuários criados em
uma tabela, de acordo com o template listar_usuarios.html
A coluna "Senha" deve exibir o valor dos 5 primeiros caracteres do hash
da senha do usuário, seguidos de reticências ("..."), e não a senha em si.
Ex.:
    Senha: "123", hash_string("123") ->
        "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"
    Deve exibir apenas: a665a...

"""

user_1 = Users('Ernesto', 'ernesto@codar.me', '123')
user_2 = Users('Alice', 'alice@codar.me', '12345')
user_3 = Users('Mateus', 'mateus@codar.me', '54321')
user_4 = Users('Maria', 'maria@codar.me', '7653')
user_5 = Users('Marcia', 'marcia@codar.me', '983234')

list_users = [user_1, user_2, user_3, user_4, user_5]


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/users/':
            self.send_response(200)

            self.send_header("Content-Type", "text/html; charset=utf-8")

            self.end_headers()

            users_informations = ""

            for user in list_users:
                users_informations += f"""
                    <tr>
                        <td>{user.user_id}</td>
                        <td>{user.name}</td>
                        <td>{user.email}</td>
                        <td>{user.hash_string()}</td>
                    </tr>
                """

            stylesheet = """\
                <style>
                    table {
                        border-collapse: collapse;
                    }

                    td, th {
                        border: 1px solid #dddddd;
                        text-align: left;
                        padding: 8px;
                    }
                </style>
            """

            data = f"""\
                <html>
                    <head>
                        {stylesheet}
                    </head>
                    <h1>Usuários</h1>
                    <table>
                        <thead>
                            <tr>
                                <th>Id</th>
                                <th>Nome</th>
                                <th>Email</th>
                                <th>Senha</th>
                            </tr>
                        </thead>
                        <tbody>
                            {users_informations}
                        </tbody>
                    </table>
                </html>
            """

            self.wfile.write(data.encode())

        elif self.path == '/API/users/':
            self.send_response(200)

            self.send_header("Content-Type", "application/json; charset=utf-8")

            self.end_headers()

            users_informations = []

            for user in list_users:
                users_informations.append({
                    "id": user.user_id,
                    "name": user.name,
                    "email": user.email,
                    "password": user.password,
                })

            data = json.dumps(users_informations).encode()
            self.wfile.write(data)


server = HTTPServer(('localhost', 8000), SimpleHandler)

print('http://localhost:8000/users/')
server.serve_forever()
