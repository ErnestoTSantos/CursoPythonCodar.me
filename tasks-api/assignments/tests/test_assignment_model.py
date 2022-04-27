from assignments.models import Assignment
from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class TestAssignmentModel(APITestCase):
    def test_name_returned(self):
        clovis = User.objects.create(
            username="Clovis", password="12345", email="Clovis@gmail.com"
        )

        assignment = Assignment.objects.create(
            creator=clovis,
            task_name="Conseguir um bom emprego",
            create_day="2022-05-20",
        )

        assert str(assignment) == "Clovis -> Conseguir um bom emprego"
