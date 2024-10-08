# Multiplicador de preço
# Mostra a tabela de preços
print('Tabela de Preços')
preco_produto = 1.99
# Quantidade entre 1 e 50
for quantidade in range(1, 51):
    valor_total = quantidade * preco_produto
    print(quantidade, '- R$', format(valor_total, '.2f')) # .2f seria para colocar duas casas decimais ante o valor
