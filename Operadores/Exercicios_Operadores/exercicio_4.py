buy_value = float(input('Digite o valor da compra: '))
cost_freight = float(input('Digite o valor do frete: '))
registered = input('O cliente é cadastrado? (S/N): ').upper()

if buy_value + cost_freight > 100:
    print('O desconto pode ser utilizado!')
elif registered == 'S':
    print('O desconto pode ser utilizado!')
else:
    print('O desconto não pode ser aplicado!')
