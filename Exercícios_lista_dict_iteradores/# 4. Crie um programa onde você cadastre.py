# 4. Crie um programa onde você cadastre a data de nascimento (dd/mm/aa) de algumas celebridades em um dicionário. 
# Ao escolher uma celebridade, seu programa deve retornar a data completa. 
# Não esqueça de validar se a celebridade escolhida está presente em seu dicionário.

from datetime import datetime

ano_atual = datetime.today().year
celebridades = {'Jose' : '21/08/1990', 'Maria' : '06/03/1959', 'Pedro' : '12/07/1943', 'Joao' : '15/12/1945'}
print('Seja bem vindo a nosso calendário. Digite o nome da celebridade exibido abaixo: ')
for celebridade in celebridades:
    print(celebridade)
opc = 1
while opc == 1:
    nome = input('Digite o nome da celebridade: ').strip().capitalize()
    while nome not in celebridades:
        print(f'Não temos a data de nascimento do(a) {nome}, tente outro nome: ')
        nome = input('Digite o nome da celebridade: ').strip().capitalize()

    ano_nascimento = int(celebridades[nome][-4:])
    idade = ano_atual - ano_nascimento
    print(f'A celebridade {nome} nasceu em {celebridades[nome]} e possui {idade} anos de idade!')

    resp = input('Deseja saber a data de ourta pessoa? [s/n]').strip().lower()
    while resp != 's' and resp != 'n':
        print('Resposta Inválida, digite novamente!')
        resp = input('Deseja saber a data de ourta pessoa? [s/n]').strip().lower()
    if resp == 'n':
        print('Fim do programa.')
        opc = 0


