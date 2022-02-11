"""

Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto uma
tupla quanto um dicionário. Dica: método type pode te ajudar.

"""


def biggerAge(person):
    name = None
    age = None

    if type(person) == tuple:
        name, age = person
    elif type(person) == dict:
        name = person['name']
        age = person['age']
    else:
        name = None
        age = None

    if age is None:
        return f'Não é possível coletar os valores de um {type(person)}'
    else:
        if age >= 18:
            return f'{name} é maior de idade!'
        elif age < 18:
            return f'{name} é menor de idade!'


name = input('Digite o nome: ')
age = int(input('Digite a idade: '))

combination = {
    'name': name,
    'age': age
}

verifyAgeDict = biggerAge(combination)
print(verifyAgeDict)

name = input('Digite o nome: ')
age = int(input('Digite a idade: '))

tuple_combination = [name, age]

verifyAgeTuple = biggerAge(tuple_combination)
print(verifyAgeTuple)
