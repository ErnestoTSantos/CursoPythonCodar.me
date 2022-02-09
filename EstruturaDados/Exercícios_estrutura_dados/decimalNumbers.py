"""

Data uma lista de números inteiros, escreva um programa que calcula a média dos
números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3
deve imprimir apenas 12 .

"""

elements = [1, 10, 20, 35, 22, 12]

total = 0

for element in elements:
    total += element

result = total // len(elements)

print(f'O valor da média dos números é: {result}')
