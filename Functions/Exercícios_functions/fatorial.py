"""

Uma função fatorial calcula o valor da multiplicação de um certo número
inteiro não-negativo por todos os números positivos menores que ele. A exceção
é o fatorial de zero que é igual a 1.

"""


def fatorial(num):
    if num == 0:
        return 1
    else:
        # Utilização de recursividade
        calc = num * fatorial(num - 1)
        return calc


number = int(input('Digite um número inteiro positivo: '))
fat = fatorial(number)
print(fat)
