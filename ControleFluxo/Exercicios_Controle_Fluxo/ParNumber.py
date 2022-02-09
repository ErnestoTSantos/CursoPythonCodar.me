number = int(input('Digite um número inteiro: '))

i = 1

value = []

while i <= number:
    if i % 2 == 0:
        value.append(i)
    i += 1

print('Os números pares são: ')
for j in value:
    print(j, end=' ')
