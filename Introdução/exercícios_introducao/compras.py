valor_compras = 49.99
desconto = valor_compras * 0.1
compras = 4
valor_desconto = valor_compras - desconto
preco_medio = valor_desconto / compras

print(f'O valor das compras com desconto é: R${valor_desconto:.2f}')
print(f'O custo médio por item é de: {preco_medio:.2f}')
