import unittest

from grade_calculator import GradeCalculator


class TestCalculatorNotes(unittest.TestCase):
    def create_list(self):
        students = [('Ernesto', 9.3), ('Maria', 7), ('Júlia', 10),
                    ('Carlos', 3), ('João', 8), ('Gabriel', 6.7)]
        grade = GradeCalculator(students)
        return grade

    def setUp(self) -> None:
        self.students = self.create_list()
        return super().setUp()

    def test_get_average_notes(self):
        average = self.students.get_average()
        self.assertEqual(average, 7.33)

    def test_get_highest_note(self):
        highest_note = self.students.get_highest_note()
        self.assertEqual(highest_note, 'Nome: Júlia e Nota: 10')

    def test_lowest_note(self):
        lowest_note = self.students.get_lowest_note()
        self.assertEqual(lowest_note, 'Nome: Carlos e Nota: 3')

    def test_get_approved_students(self):
        approved_people = self.students.get_approved()
        self.assertEqual(approved_people, ['Ernesto', 'Maria', 'Júlia', 'João'])  # noqa:E501

    def test_get_disapproved_students(self):
        disapproved = self.students.get_disapproved()
        self.assertEqual(disapproved, ['Carlos', 'Gabriel'])

    def test_bills_into_letters(self):
        representation = self.students.get_bills_into_letters()
        self.assertEqual(representation, [('Ernesto', 'A'), ('Maria', 'B'), (
            'Júlia', 'A+'), ('Carlos', 'D'), ('João', 'B'), ('Gabriel', 'C')])


unittest.main()
