# 6 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
 #As perguntas são:
#•"Telefonou para a vítima?"
#•"Esteve no local do crime?"
#•"Mora perto da vítima?"
#•"Devia para a vítima?"
#•"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se   a   pessoa   responder   positivamente   a   2   questões   ela   deve   ser   classificada   como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 
# 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

telefonou = input('Telefonou para a vítima? [s/n]').strip().lower()
while telefonou != 's' and telefonou != 'n':
    print('Comando inválido, digite novamente.')
    telefonou = input('Telefonou para a vítima? [s/n]').strip().lower()

esteve = input('Esteve no local do crime? [s/n]').strip().lower()
while esteve != 's' and esteve != 'n':
    print('Comando inválido, digite novamente.')
    esteve = input('Esteve no local do crime? [s/n]').strip().lower()

mora = input('Mora perto da vítima? [s/n]').strip().lower()
while mora != 's' and mora != 'n':
    print('Comando inválido, digite novamente.')
    mora = input('Mora perto da vítima? [s/n]').strip().lower()

devia = input('Devia para a vítima? [s/n]').strip().lower()
while devia != 's' and devia != 'n':
    print('Comando inválido, digite novamente.')
    devia = input('Devia para a vítima? [s/n]').strip().lower()

trabalhou = input('Já trabalhou com a vítima? [s/n]').strip().lower()
while trabalhou != 's' and trabalhou != 'n':
    print('Comando inválido, digite novamente.')
    trabalhou = input('Já trabalhou com a vítima? [s/n]').strip().lower()

respostas = [telefonou, esteve, mora, devia, trabalhou]

contador = 0
for resposta in respostas:
    if resposta == 's':
        contador += 1

if contador < 2:
    print('O individuo é Inocente')
elif contador < 3:
    print('O individuo é Suspeito')
elif contador < 5:
    print('O individuo é Cúmplice')
else:
    print('O individuo é o ASSASSINO!')