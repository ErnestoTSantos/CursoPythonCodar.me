# Escreva uma programa que calcula a média das notas de todos os alunos.


students = [{
    "nome": "Alice",
    "nota": 8,
},
    {
        "nome": "Bob",
        "nota": 7,
},
    {
        "nome": "Carlos",
        "nota": 9,
}
]

total = 0

for i in students:
    note = i["nota"]
    total += note

result = total / len(students)
print(f'A média das notas dos alunos é: {result:.2f}')
