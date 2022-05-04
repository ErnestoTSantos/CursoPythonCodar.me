import json

from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TestUserView(APITestCase):
    def test_status_check(self):
        request = self.client.get("/api/user/")

        assert request.status_code == 200

    def test_list_users(self):
        clovis = User.objects.create_user(
            username="Clovis", password="12345", email="clovis@gmail.com", is_staff=True
        )
        self.client.force_authenticate(clovis)
        request = self.client.get("/api/user/list_users/")
        data = json.loads(request.content)

        email = data[0]["email"]
        first_name = data[0]["first_name"]
        last_name = data[0]["last_name"]
        id = data[0]["id"]
        is_staff = data[0]["is_staff"]
        username = data[0]["username"]

        assert email == "clovis@gmail.com"
        assert first_name == ""
        assert id == 1
        assert is_staff is True
        assert last_name == ""
        assert username == "Clovis"

    def test_first_name_is_less(self):
        user = {
            "username": "Clovis",
            "first_name": "Et",
            "last_name": "Santos",
            "email": "clovis@gmail.com",
            "password": "24042022",
        }

        post = self.client.post("/api/user/create_user/", user)

        assert post.status_code == 400
        assert post.data[0] == "O primeiro nome precisa ter mais de 3 caracteres!"

    def test_create_user(self):
        user = {
            "username": "clóvis",
            "first_name": "Ernesto",
            "last_name": "Santos",
            "email": "clovis@gmail.com",
            "password": "24042022",
        }

        post = self.client.post("/api/user/create_user/", user)

        assert post.status_code == 201

    def test_create_user_without_username(self):
        user = {
            "username": "",
            "first_name": "Ernesto",
            "last_name": "Santos",
            "email": "clovis@gmail.com",
            "password": "24042022",
        }

        post = self.client.post("/api/user/create_user/", user)

        assert post.status_code == 400
        assert post.data[0] == "É necessário ter um nome de usuário!"

    def test_create_user_without_password(self):
        user = {
            "username": "Clovis",
            "first_name": "Ernesto",
            "last_name": "Santos",
            "email": "clovis@gmail.com",
            "password": "",
        }

        post = self.client.post("/api/user/create_user/", user)

        assert post.status_code == 400
        assert post.data[0] == "É necessário ter uma senha para o usuário!"

    def test_create_user_without_email(self):
        user = {
            "username": "Clovis",
            "first_name": "Ernesto",
            "last_name": "Santos",
            "email": "",
            "password": "24042022",
        }

        post = self.client.post("/api/user/create_user/", user)

        assert post.status_code == 400
        assert post.data[0] == "É necessário ter um e-mail para o usuário!"

    def test_create_user_without_first_name(self):
        user = {
            "username": "Clovis",
            "first_name": "",
            "last_name": "Santos",
            "email": "clovis@gmail.com",
            "password": "24042022",
        }

        post = self.client.post("/api/user/create_user/", user)

        assert post.status_code == 400
        assert post.data[0] == "É necessário ter um primeiro nome!"

    def test_create_user_without_last_name(self):
        user = {
            "username": "Clovis",
            "first_name": "Ernesto",
            "last_name": "",
            "email": "clovis@gmail.com",
            "password": "24042022",
        }

        post = self.client.post("/api/user/create_user/", user)

        assert post.status_code == 400
        assert post.data[0] == "É necessário ter um sobrenome!"

    def test_error_user_exist(self):
        user = {
            "username": "Clovis",
            "first_name": "Ernesto",
            "last_name": "Santos",
            "email": "clovis@gmail.com",
            "password": "24042022",
        }

        self.client.post("/api/user/create_user/", user)

        user = {
            "username": "Clovis",
            "first_name": "Ernesto",
            "last_name": "Santos",
            "email": "clovisPlayer@gmail.com",
            "password": "24042022",
        }
        post = self.client.post("/api/user/create_user/", user)

        assert post.status_code == 400
        assert post.data[0] == "O nome de usuário enviado já existe!"

    def test_error_email_exist(self):
        user = {
            "username": "Clovis",
            "first_name": "Ernesto",
            "last_name": "Santos",
            "email": "clovis@gmail.com",
            "password": "24042022",
        }

        self.client.post("/api/user/create_user/", user)

        user = {
            "username": "Squarc",
            "first_name": "Ernesto",
            "last_name": "Santos",
            "email": "clovis@gmail.com",
            "password": "24042022",
        }
        post = self.client.post("/api/user/create_user/", user)

        assert post.status_code == 400
        assert post.data[0] == "O e-mail enviado já está em uso!"
