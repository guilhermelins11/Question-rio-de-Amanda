# O valor do salario inicial entre 1996 e 2025
salario_inicial = 1000.0
aumento_anual_do_salario = 1.5 / 100
# Contagem entre os anos 1996 a 2025
for ano in range(1996, 2026):
        salario_inicial = salario_inicial + (salario_inicial * aumento_anual_do_salario)
        aumento_anual_do_salario = aumento_anual_do_salario * 2
# Mostra o valor em 2025       
print ('Salário será de R$', format(salario_inicial, '.2f'), 'em 2025') # .2f seria para colocar duas casas decimais ante o valor

# Salário será R$ 521678872372965470535091993624533602402702219041505716918642386185896096032600478449664.00 em 2025