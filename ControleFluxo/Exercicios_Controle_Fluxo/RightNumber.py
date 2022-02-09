from random import randint

number = randint(0, 10)

i = 0

print(number)

while i < 3:
    number_choice = int(input('Digite um número inteiro de 0 à 10: '))
    if number_choice < number:
        print('O número escondido é maior!')
        i += 1
    elif number_choice > number:
        print('O número escondido é menor!')
        i += 1
    elif number_choice == number:
        print('\033[35mParabéns, você ganhou!!\033[m')
        print(f'Você utilizou {i + 1} chance/chances!')
        break

if i == 3:
    print('Infelizmente você perdeu')
