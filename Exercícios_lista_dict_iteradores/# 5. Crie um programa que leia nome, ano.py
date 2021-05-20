# 5.	Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import datetime 
ano = datetime.today().year

cadastro_pessoas = {}
opc = 1
while opc == 1:
    nome = input('Digite seu nome: ')
    ano_nascimento = int(input('Digite o ano de seu nascimento (AAAA): '))
    ctps = int(input('Digite o numero de sua carteira de trabalho(caso não tenha, digite 0): '))
    idade = ano - ano_nascimento
    idade_aposentadoria = 35
    cadastro_pessoas = {nome : [ano_nascimento, ctps, idade, idade_aposentadoria]}

    if ctps != 0:
        ano_contratacao = int(input('Digite o ano que você foi contratado: '))
        salario = float(input('Qual o seu salário: '))
        cadastro_pessoas.update({nome : [ano_nascimento, ctps, ano_contratacao, salario]})
        idade_aposentadoria = idade_aposentadoria - (ano - ano_contratacao)
        cadastro_pessoas = {nome : [ano_nascimento, ctps, idade, salario, idade_aposentadoria]}
        print('----'*15)
        print(f'Nome          : {nome}')
        print(f'Idade         : {cadastro_pessoas[nome][2]}')
        print(f'Nº CTPS       : {cadastro_pessoas[nome][1]}')
        print(f'Salário       : {cadastro_pessoas[nome][3]}')
        print(f'Aposentadoria : {cadastro_pessoas[nome][4]}')
    else:
        print('----'*15)
        print(f'Nome          : {nome}')
        print(f'Idade         : {cadastro_pessoas[nome][2]}')
        print(f'Nº CTPS       : {cadastro_pessoas[nome][1]}')
        print(f'Aposentadoria : {cadastro_pessoas[nome][3]}')
    resp = input('Deseja realizar outra consulta? [s/n]').lower()
    while resp != 's' and resp != 'n':
        print('Resposta inválida, digite novamente')
        resp = input('Deseja realizar outra consulta? [s/n]').lower()
    if resp == 'n':
        print('fim do progrma')
        opc = 0
