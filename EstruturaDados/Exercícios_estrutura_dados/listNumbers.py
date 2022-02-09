"""

Escreva um programa que lê números inteiros positivos do usuário, um após o
outro, e monta uma lista a partir desses números e depois imprime a lista montada. # noqa: E501
O programa deve continuar solicitando por números até que o elemento digitado
seja um número negativo (que não deve ser inserido na lista).

"""

numbers = []

while True:
    number = int(input('Digite um número: Para finalizar as adições à lista digite um número negativo: ').strip())  # noqa: E501

    if number < 0:
        break
    else:
        numbers.append(number)

print(numbers)
