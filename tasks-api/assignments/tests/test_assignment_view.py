import json

from assignments.models import Assignment
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TestingAssignmentView(APITestCase):
    def test_get_empty_assignment_list(self):
        user = User.objects.create(username="Ernesto", password="12345")
        self.client.force_authenticate(user)
        request = self.client.get("/api/assignment/list_assignments/?username=Ernesto")
        data = json.loads(request.content)

        assert data == []

    def test_get_assignment_list(self):
        user = User.objects.create(username="Ernesto", password="12345")
        self.client.force_authenticate(user)

        Assignment.objects.create(creator=user, task_name="Criar projeto to-do")

        request = self.client.get("/api/assignment/list_assignments/?username=Ernesto")
        data = json.loads(request.content)

        assignment_return = {
            "active": True,
            "create_day": "2022-04-27",
            "creator": "Ernesto",
            "description": "",
            "id": 1,
            "task_name": "Criar projeto to-do",
            "final_day": None,
        }

        assert data[0] == assignment_return

    def test_list_assignments_with_staff_user(self):
        clovis = User.objects.create(username="Clovis", password="12345")
        Assignment.objects.create(
            creator=clovis,
            task_name="Conseguir um bom emprego",
            create_day="2022-05-20",
        )

        ernesto = User.objects.create(
            username="Ernesto", password="12345", is_staff=True
        )
        self.client.force_authenticate(ernesto)

        request = self.client.get("/api/assignment/list_assignments/")

        assert request.status_code == 200

    def test_post_assignment(self):
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


class TestStatusCheck(APITestCase):
    def test_assignment_status_check(self):
        request = self.client.get("/api/assignment/")

        assert request.status_code == 200
