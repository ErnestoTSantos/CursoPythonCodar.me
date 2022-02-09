on = 'S'

while on == 'S':
    operating_1 = float(input('Digite um operando: '))
    operating_2 = float(input('Digite outro operando: '))
    operator = input('Digite o operador: ')

    if operator == '+':
        print(f'O resultado da soma é: {operating_1 + operating_2:.2f}')
    elif operator == '-':
        print(f'O resultado da subtração é: {operating_1 - operating_2:.2f}')
    elif operator == '*':
        print(
            f'O resultado da multiplicação é: {operating_1 * operating_2:.2f}')
    elif operator == '/':
        if operating_2 == 0.0:
            print('Não é possível realizar divisão por zero!')
        else:
            print(f'O resultado da divisão é: {operating_1 / operating_2:.2f}')

    on = input('Deseja realizar mais operações? (S/N): ')
