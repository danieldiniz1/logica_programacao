# Desafio Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre:
#A) Quantas pessoas estão cadastradas.
#B) A média da idade.
#C) Uma lista com as mulheres.
#D) Uma lista com as idades que estão acima da média.
#OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

cadastro_geral = {}
cadastro_mulheres = []

opc = 1
while opc == 1:
    nome = input('Digite seu nome: ').lower().title()
    sexo = input('Digite seu sexo (F para feminino e M para Masculino): ').upper()
    while sexo != 'F' and sexo != 'M':
        print('Sexo inválido, digite novamente.')
        sexo = input('Digite seu sexo (F para feminino e M para Masculino): ').upper()
    idade = int(input('Digite sua idade: '))
    while idade < 0:
        print('Idade Inválida, digite novamente!')
        idade = int(input('Digite sua idade: '))
    cadastro_geral.update({nome : [sexo, idade]})
    if sexo == 'F':
        cadastro_mulheres.append(nome)
    resp = input('Deseja adicionar outra pessoa? [S/N]').upper()
    while resp != 'S' and resp != 'N':
        print('Comando inválido, digite novamente.')
        resp = input('Deseja adicionar outra pessoa? [S/N]').upper()
    if resp == 'N':
        print('fim do programa')
        opc = 0

print(cadastro_geral)
print('------'*15)
print()

print(f'A quantidade de pessoas cadastradas é de {len(cadastro_geral)} pessoas.')

soma_idade = 0
for pessoa in cadastro_geral:
    soma_idade += cadastro_geral[pessoa][1]
media_idade_geral = soma_idade / len(cadastro_geral)
print(f'A idade média das pessoas cadastradas é {media_idade_geral:.0f} anos.')

print(cadastro_mulheres) #lista de mulheres

for pessoa in cadastro_geral:
    if cadastro_geral[pessoa][1] > media_idade_geral:
        print(f'A {pessoa} tem a idade de {cadastro_geral[pessoa][1]} anos que é acimda da média de {media_idade_geral:.0f} anos!')

