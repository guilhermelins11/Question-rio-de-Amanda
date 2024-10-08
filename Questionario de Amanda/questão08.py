# Estrutura de verificação de gabarito de prova
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
notas = []  # Lista para armazenar as notas dos alunos
quantidade_total_alunos = 0  # Contador de alunos

# iteração = sequencia para coletar respostas dos alunos
while True:
    acertos = 0  # Contador de acertos do aluno
    print("\nResponda as perguntas (A, B, C, D, E):")
    
    # Mostra as perguntas
    for i in range(10):
        resposta = input('Questão ' + str(i + 1) + ': ').upper()  
        if resposta == gabarito[i]:  
            # Coloca a quantidade de acertos
            acertos += 1
           
    # Acertos de cada aluno
    notas.append(acertos)  
    # quantidade total de aluno
    quantidade_total_alunos += 1  
    
    # Pergunta se outro aluno quer responder
    continuar = input('Outro aluno vai responder? (sim/nao): ').lower()
    if continuar != 'sim':  
      # essa tag acaba com a sequencia se a resposta for nao
        break  

# Mostrar resultados 
if quantidade_total_alunos > 0:  
    # Mostra o a quantidade total de alunos
    print('\nTotal de alunos: ' + str(quantidade_total_alunos)) 
    
    # Mostra a maior nota
    print('Maior acerto: ' + str(max(notas))) 
    
    # Mostra a menor nota 
    print('Menor acerto: ' + str(min(notas)))  
    
    media_de_acertos_por_aluno = sum(notas) / quantidade_total_alunos
      
    print('Média de acertos: ' + str(media_de_acertos_por_aluno))  
else:
    #se não tiver nenhuma resposta, ele mostra a mensage abaixoa
    print('Nenhum aluno respondeu.')  
