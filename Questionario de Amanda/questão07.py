# Tabela dinamica sobre uma divida
valor_divida = 1000
porcentagem_juros = [0, 0.10, 0.15, 0.20, 0.25]
numero_parcelas = [1, 3, 6, 9, 12]

# Mostrar a tabela de dívidas
print("\n| Dívida  | Juros   | Parcelas | Valor da Parcela |")
for i in range(len(numero_parcelas)):
    valor_juros = valor_divida * porcentagem_juros[i]
    total_divida = valor_divida + valor_juros
    valor_parcela = total_divida / numero_parcelas[i]
    
    # Exibe as informações em formato de tabela                     # format permite organizar as strings separadamente, e colocar a quantidade de casas decimais mostrar.
    print('| R$ {:.2f} | {:.0f}%   | {}x     | R$ {:.2f}      |'.format(total_divida, porcentagem_juros[i] * 100, numero_parcelas[i], valor_parcela))


    
    
    
    

    
