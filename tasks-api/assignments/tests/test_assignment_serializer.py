from datetime import date

from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TestAssignmentSerializer(APITestCase):
    def test_creator_validation_exists(self):
        clovis = User.objects.create(
            username="Clovis", password="12345", email="Clovis@gmail.com"
        )

        assignment = {
            "creator": "Clovis",
            "task_name": "Fazer prova de cálculo 1",
        }

        self.client.force_login(clovis)
        request_post = self.client.post("/api/assignment/list_assignments/", assignment)

        assert request_post.status_code == 201

    def test_creator_validation_not_exists(self):
        clovis = User.objects.create(
            username="Clovis", password="12345", email="Clovis@gmail.com"
        )

        assignment = {
            "creator": "Ernesto",
            "task_name": "Fazer prova de cálculo 1",
        }

        self.client.force_login(clovis)
        request_post = self.client.post("/api/assignment/list_assignments/", assignment)

        assert request_post.data["creator"][0] == "O criador informado não existe!"

    def test_task_name_validation_chars_less_quantity(self):
        clovis = User.objects.create(
            username="Clovis", password="12345", email="Clovis@gmail.com"
        )

        assignment = {
            "creator": "Clovis",
            "task_name": "FaZe",
        }

        self.client.force_login(clovis)
        request_post = self.client.post("/api/assignment/list_assignments/", assignment)

        assert (
            request_post.data["task_name"][0]
            == "O nome da tarefa precisa ter 5 ou mais caracteres!"
        )

    def test_task_name_validation_not_empty(self):
        clovis = User.objects.create(
            username="Clovis", password="12345", email="Clovis@gmail.com"
        )

        assignment = {
            "creator": "Clovis",
            "task_name": "",
        }

        self.client.force_login(clovis)
        request_post = self.client.post("/api/assignment/list_assignments/", assignment)

        assert request_post.data["task_name"][0] == "This field may not be blank."

    def test_final_day_in_past(self):
        clovis = User.objects.create(
            username="Clovis", password="12345", email="Clovis@gmail.com"
        )

        assignment = {
            "creator": "Clovis",
            "task_name": "Fazer prova de cálculo 1",
            "final_day": "2022-03-29",
        }

        self.client.force_login(clovis)
        post = self.client.post("/api/assignment/list_assignments/", assignment)

        assert (
            post.data["final_day"][0]
            == "A finalização não pode ser realizada no passado!"
        )
