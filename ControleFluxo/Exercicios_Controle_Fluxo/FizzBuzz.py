on = 'S'

while on == 'S':
    number = int(input('Digite um número inteiro: '))

    if (number % 3) == 0 and (number % 5) == 0:
        print('FizzBuzz')
    elif (number % 3) == 0:
        print('Fizz')
    elif (number % 5) == 0:
        print('Buzz')

    on = input('Deseja digitar mais um número? (S/N): ').upper()
