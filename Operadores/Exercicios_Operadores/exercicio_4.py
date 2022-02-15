buy_value = float(input('Digite o valor da compra: '))
cost_freight = float(input('Digite o valor do frete: '))
registered = input('O cliente é cadastrado? (S/N): ').upper()

verifyPurchasesValues = buy_value + cost_freight >= 100
verifyRegister = registered == 'S'
verifyResult = verifyPurchasesValues or verifyRegister

print(f'O desconto poderá ser aplicado: {verifyResult}')
