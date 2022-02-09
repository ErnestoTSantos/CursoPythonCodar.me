number = int(input('Digite um número: '))

i = 1
j = 0


while i <= number:

    if (number % i) == 0:
        j += 1

    i += 1

if j == 2:
    print(f'O número {number} é primo!')
else:
    print(f'O número {number} não é primo!')
