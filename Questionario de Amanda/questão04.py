# Calculo doe crescimento para que a População do Pais A Ultrapasse ou Alcance a População do Pais B.
pais_A = 80000
pais_B = 200000
crescimentopopulacional_A = 0.03
crescimentopopulacional_B = 0.015
tempo = 0

while pais_A < pais_B:
    pais_A = pais_A + (pais_A * crescimentopopulacional_A)
    pais_B = pais_B + (pais_B * crescimentopopulacional_B)
    tempo = tempo + 1
# Mostra a duração em anos para que o Pais A alcance ou ultrapasse o Pais B.
print('Sera preciso', tempo, 'anos para que a população do pais A ultrapasse ou alcance a população do pais B.')

# Resposta: "Sera preciso 63 anos para que a população do pais A ultrapasse ou alcance a população do pais B."