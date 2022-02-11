"""

Implemente uma função que recebe uma lista de números inteiros e retorna uma
tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e
num é o valor desse número.

"""


def returnTuple(list_num: list):

    num = 0
    position = 0

    amount_numbers = len(list_num)

    for pos in range(0, amount_numbers):

        if list_num[pos] > num:
            num = list_num[pos]
            position = pos

    return (position, num)


elements = [5, 4, 8.9, 78, 19, 35, 20, 74]
biggestNumber = returnTuple(elements)
print(biggestNumber)
