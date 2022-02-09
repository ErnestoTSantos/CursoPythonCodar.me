# Escreva uma programa que calcula a média das notas de todos os alunos.

students = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9),
]

total = 0

for student, note in students:
    total += note


average = total / len(students)
print(f'A média de nota dos alunos é: {average:.2f}')
