# Pede que o usuário escreva um número para que seja feito a multiplicação
numero = int(input('Digite um número para ver a tabuada: '))

# Mostra a multiplicação do numero
for m in range(10):
    resultado = numero * (m + 1)
    print(numero, 'x', m + 1, '=', resultado)