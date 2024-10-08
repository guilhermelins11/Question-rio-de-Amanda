# Verificar se o numero escrito é um numero primo.
def verificar_primo(n):
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True

numero = int(input('Informe um número: '))
resultado = verificar_primo(numero)
# Mostra se o numero é ou não um numero primo.
if resultado:
    print(numero, 'é um número primo.')
else:
    print(numero, 'não é um número primo.')
