"""
CALCULADORA DE NOTAS
====================
1. Recebe uma turma, composta por uma lista de Alunos(nome, nota) e média para aprovar um aluno. # noqa:E501
2. Calcula a média das notas da turma (get_media).
3. Qual a maior e menor nota (get_maior_nota, get_menor_nota).
4. Retorna alunos aprovados e reprovados (get_aprovados, get_reprovados).
5. Retorna lista de notas em representação de "letra".
    - nota == 10       =>    "A+"
    - 9 <= nota < 10   =>    "A"
    - 7 <= nota < 9    =>    "B"
    - 5 <= nota < 7    =>    "C"
    - 3 <= nota < 5    =>    "D"
    - 1 <= nota < 3    =>    "E"
    - 0 <= nota < 1    =>    "F
"""


class GradeCalculator:
    def __init__(self, students: list):
        self._students = students

    def get_average(self):
        students_amount = len(self._students)
        average = 0
        for student, note in self._students:
            average += note

        return round(average/students_amount, 2)

    def get_highest_note(self):
        list_students = self._students

        def highest_note(object):
            student, note = object

            return note

        list_students.sort(key=highest_note)

        students_amount = len(list_students)

        return f'Nome: {list_students[students_amount - 1][0]} e Nota: {list_students[students_amount - 1][1]}'  # noqa:E501

    def get_lowest_note(self):
        list_students = self._students

        def lowest_note(object):
            student, note = object

            return note

        list_students.sort(key=lowest_note)

        return f'Nome: {list_students[0][0]} e Nota: {list_students[0][1]}'

    def get_approved(self):
        approved_students = []

        for student, note in self._students:
            if note >= 7:
                approved_students.append(student)

        return approved_students

    def get_disapproved(self):
        disapproved_students = []

        for student, note in self._students:
            if note < 7:
                disapproved_students.append(student)

        return disapproved_students

    def get_bills_into_letters(self):
        notes = []
        for student, note in self._students:
            if note == 10:
                note = 'A+'
            elif 9 <= note < 10:
                note = 'A'
            elif 7 <= note < 9:
                note = 'B'
            elif 5 <= note < 7:
                note = 'C'
            elif 3 <= note < 5:
                note = 'D'
            elif 1 <= note < 3:
                note = 'E'
            else:
                note = 'F'

            notes.append((student, note))

        return notes
