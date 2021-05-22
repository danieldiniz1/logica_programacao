# 8 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import datetime
ano_atual = datetime.today().year

def verifica_numero():
    numero = ''
    opc = 1
    while opc == 1:
        try:
            numero = int(input('Digite o valor: '))
        except:
            print('valor inválido, apenas números devem ser digitados')
        if numero != '':
            opc = 0
    return numero

opc = 1
individuos = {}
while opc == 1:
    nome = input('Digite seu nome: ').strip().capitalize()

    print('Qual seu ano de Nascimento?')
    ano_nascimento = verifica_numero()
    while len(str(ano_nascimento)) != 4:
        print('O ano deve conter 4 digitos "AAAA". ')
        ano_nascimento = verifica_numero()

    print('Qual o número de sua Carteira de Trabalho? [Digite 0 caso não tenha]')
    ctps = verifica_numero()

    idade = ano_atual - ano_nascimento
    idade_aposentadoria = 35
    ano_contratacao = ''
    salario = ''
    
    if ctps != 0:
        print('Qual o ano que você foi contratado?')
        ano_contratacao = verifica_numero()
        idade_aposentadoria -= ano_atual - ano_contratacao
        
        opc_salario = 1
        salario = ''
        while opc_salario == 1:  
            try:
                salario = float(input('Qual é o valor do seu salário?'))
            except:
                print('Salário inválido, digite apenas números.')
            if salario != '':
                opc_salario = 0

    individuos.update({nome : [ano_nascimento, idade, idade_aposentadoria, ano_contratacao, salario]})

    resp = input('Deseja incluir uma nova pessoa? [s/n]').strip().lower()
    while resp != 's' and resp != 'n':
        print('Resposta inválida, digite novamente. ')
        resp = input('Deseja incluir uma nova pessoa? [s/n]').strip().lower()
    if resp == 'n':
        opc = 0
    
print('-'*50)
for pessoa in individuos:
  if individuos[pessoa][3] == '':
    print(f'{pessoa} tem {individuos[pessoa][1]} anos de idade e nasceu em {individuos[pessoa][0]}. Irá se aposentar com {individuos[pessoa][2]} anos de trabalho.')
    print('-'*50)
  elif individuos[pessoa][2] <= 0:
    print(f'{pessoa} tem {individuos[pessoa][1]} anos de idade e nasceu em {individuos[pessoa][0]}. Está aposentada pois começou a trabalhar em {individuos[pessoa][3]} com um salário de R$ {individuos[pessoa][4]:.2f}')
    print('-'*50)  
  else:
    print(f'{pessoa} tem {individuos[pessoa][1]} anos de idade e nasceu em {individuos[pessoa][0]}. Irá se aposentar em {individuos[pessoa][2]} anos pois começou a trabalhar em {individuos[pessoa][3]} com um salário de R$ {individuos[pessoa][4]:.2f}')
    print('-'*50)