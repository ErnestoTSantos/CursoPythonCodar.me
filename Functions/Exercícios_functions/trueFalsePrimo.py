"""
Escreva uma função que recebe um número inteiro positivo e retorna True
caso ele seja primo e False, caso contrário.
"""


def e_primo(value):

    j = 0

    for number in range(1, value + 1):

        if (value % number) == 0:
            j += 1

    if j == 2:
        return True
    else:
        return False


number = int(input('Digite um valor: '))
value = e_primo(number)
print(f'{number} é um número primo: {value}')
