#  3. Uma escola te contratou para desenvolver um programa em Python para que o professor gerencie as notas de seus alunos. Seu programa deve apresentar o seguinte menu:
#0. Sair ok
#1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
#2. Inserir aluno e nota
#3. Alterar a nota de um aluno
#4. Consultar nota de um aluno específico 
#5. Apagar um aluno da lista
#6. Exibir a média da turma
#As notas e os nomes dos alunos serão fornecidos pelo professor. Implemente a sua solução utilizando dicionário.

opcoes = list(range(7))
lista_opcoes = ['0. Sair', 
                '1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)',
                '2. Inserir aluno e nota',
                '3. Alterar a nota de um aluno', 
                '4. Consultar nota de um aluno específico',
                '5. Apagar um aluno da lista',
                '6. Exibir a média da turma']
notas_classe = {}
lista_notas_classe = []
lista_alunos = []
opc = 1
while opc == 1: 
    for atividade in lista_opcoes:
        print(atividade)
    opcao = int(input('Digite a opção desejada: '))
    
    while opcao not in opcoes:
        print('Opção Inválida, digite novamente!')
        opcao = int(input('Digite a opção desejada: '))
    
    if opcao == 0: # Sair
        print('---'*15)
        print('Fim do programa, obrigado por utilizar!')
        opc = 0
    
    elif opcao == 1: #Exibir lista de alunos com suas notas (cada aluno tem uma nota)
        print('---'*15)
        for aluno in notas_classe:
            print(f'O aluno(a) {aluno} obteve a nota {notas_classe[aluno]},')
        print('---'*15)
    
    elif opcao == 2: # Inserir aluno e nota
        nome_aluno = input('Digite o nome do aluno: ').strip().capitalize()
        nota_aluno = float(input(f'Digite a nota do aluno: '))
           
        notas_classe.update({nome_aluno : nota_aluno})
        lista_notas_classe.append(nota_aluno)
        lista_alunos.append(nome_aluno)
        print('---'*15)
        print(f'O aluno {nome_aluno} com nota {nota_aluno} foi cadastrado com sucesso!')
        print('---'*15)
    
    elif opcao == 3: # Alterar a nota de um aluno
        nome_aluno = input('Digite o nome do aluno que quer alterar a nota: ').strip().capitalize()
        nota_aluno = float(input(f'Digite a nova nota do aluno: '))
        if nome_aluno not in notas_classe:
            print('---'*15)
            print(f'O aluno {nome_aluno} não foi cadastrado. utilize a opção 2 para cadastrar')
        else:
            notas_classe.update({nome_aluno : nota_aluno})
            indice = lista_alunos.index(nome_aluno)
            lista_notas_classe[indice] = nota_aluno
            print('---'*15)
            print(f'Nota do aluno {nome_aluno} alterada para {nota_aluno} com sucesso!')
        print('---'*15)

    elif opcao == 4: #Consultar nota de um aluno específico
        nome_aluno = input('Digite o nome do aluno que deseja consultar a nota: ').strip().capitalize()
        if nome_aluno not in notas_classe:
            print('---'*15)
            print(f'O aluno {nome_aluno} não foi cadastrado. utilize a opção 2 para cadastrar')
        else:
            print('---'*15)
            print(f'O aluno {nome_aluno} obteve a nota {notas_classe[nome_aluno]}')
        print('---'*15)
    
    elif opcao == 5: # Apagar um aluno da lista
        nome_aluno = input('Digite o nome do aluno: ').strip().capitalize()
        if nome_aluno not in notas_classe:
            print('---'*15)
            print(f'O aluno {nome_aluno} não foi cadastrado. utilize a opção 2 para cadastrar')
        else:
            notas_classe.pop(nome_aluno)

            indice = lista_alunos.index(nome_aluno)
            lista_notas_classe.pop(indice)
            lista_alunos.pop(indice)
            print('---'*15)
            print(f'Aluno {nome_aluno} excluído com sucesso!')
        print('---'*15)
    
    elif opcao == 6: # Exibir a média da turma
        if len(lista_alunos) == 0:
            print('---'*15)
            print('Não foi possível calcular a média pois não tem alunos cadastros. Cadastre na Opção 2!')
            print('---'*15)
        else: 
            media = sum(lista_notas_classe) / len(lista_alunos)
            print('---'*15)
            print(f'A média da sala é {media:.2f},')
            print('---'*15)
