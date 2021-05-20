#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela. 
# A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado. 
# Para resolver esse desafio consultar o link sobre funções em dicionários que foi disponibilizado.

notas_alunos = {}

opc = 1
while opc == 1:
    nome = input('Digite o nome do aluno: ')
    media = float(input('Digite a nota do aluno: '))
    while media < 0:
        print('Média Inválida, tente novamente!')
        media = float(input('Digite a nota do aluno: '))

    notas_alunos.update({nome : media})
    resp = input('Deseja adicionar outro aluno? [s/n]').lower()
    while resp != 's' and resp != 'n':
        print('Resposta inválida, digite novamente')
        resp = input('Deseja adicionar outro aluno? [s/n]').lower()
    if resp == 'n':
        print('As médias estão sendo processadas e os resultados estão abaixo:')
        opc = 0

print(notas_alunos)

for media in notas_alunos:
    if notas_alunos[media] >= 7:
        print('Aluno Aprovado')
    elif notas_alunos[media] < 5:
        print('Aluno Reprovado')
    else:
        print('Aluno em Recuperação')