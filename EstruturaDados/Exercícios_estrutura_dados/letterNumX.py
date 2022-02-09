"""

Escreva um programa que solicite uma string para o usuário e imprima quantas
vezes cada letra aparece na palavra.

"""

word = input('Digite uma palavra: ').lower()

list_letters: dict[str, int] = {}

for letter in word:
    if letter in list_letters:
        list_letters[letter] += 1
    else:
        list_letters[letter] = 1

print(list_letters)
