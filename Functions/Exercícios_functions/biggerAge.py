"""

Implemente uma função maior_idade(pessoa) que receba uma tupla representando
uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou
não

"""


def biggerAge(person: tuple):
    name, age = person

    if age >= 18:
        return f'{name} é maior de idade!'
    else:
        return f'{name} é menor de idade!'


name = input('Digite o nome: ')
age = int(input('Digite a idade: '))

combination = (name, age)

verifyAge = biggerAge(combination)
print(verifyAge)
