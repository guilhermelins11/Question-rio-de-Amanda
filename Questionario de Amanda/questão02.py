# Contador de numeros impares, e pares.
total_pares = 0
total_impares = 0

for n in range(10):
    num = int(input('Digite um número: '))
    
    if num % 2 == 0:
        total_pares += 1
    else:
        total_impares += 1
# Mostra a quantidade de numeros impares e pares.
print('Quantidade de números pares:', total_pares)
print('Quantidade de números ímpares:', total_impares)

