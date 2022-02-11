"""

Implemente uma função que recebe dois argumentos, uma lista e um elemento , e
retorna True caso elemento seja encontrado na lista , e False caso contrário.
Não é permitido utilizar o método in.

"""


def elementInList(list, comparation):

    value = False

    for i in list:
        if i == comparation:
            value = True

    return value


elements = [1, 10, 20, 35, 22, 12, 78, 90]
element = 78

verifyElement = elementInList(elements, element)
print(f'O elemento {element} está na lista? {verifyElement}')

elements.remove(78)
verifyElement = elementInList(elements, element)
print(f'O elemento {element} está na lista? {verifyElement}')
