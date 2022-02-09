number = int(input('Digite um número inteiro: '))

i = 1

value = 0

while i <= number:
    value += i
    i += 1

print('A soma de todos os números até {} é: {}'.format(number, value))
