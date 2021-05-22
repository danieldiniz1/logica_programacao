# 03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento. 
# Não deixe o usuário continuar se a senha estiver incorreta, 
# após entrar dê as boas-vindas a seu usuário e apresente a ele o jogo da adivinhação, onde o computador vai pensar em um número entre 0 e 10. 
# O jogador vai tentar adivinhar qual número foi escolhido até  acertar, 
# a cada palpite do usuário  diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou. 
# No final mostre quantos palpites foram necessários para vencer.

import random
from time import sleep

senha = 'D@123$'

senha_usuario = input('Digite a senha: ').strip()

while senha_usuario != senha:
    print('Senha inválida, digite novamente!')
    senha_usuario = input('Digite a senha: ')
else:
    print('Usuário, seja bem vindo ao jogo da adivinhação!')

print('---'*30)
print('Para jogar, você deve adivinhar o número que o computador escolheu digitando abaixo. boa sorte!')
print('---'*30)

numero_pc = random.randint(1,10)
numero_usuario = int(input('Digite um número de 1 a 10: '))

contador_jogadas = 1
opc = 1

while opc == 1:
    while numero_usuario > 10 or numero_usuario < 1:
        print('Número inválido, ele deve ser entre 1 e 10. Digite novamente!')
        numero_usuario = int(input('Digite um número de 1 a 10: '))
    print('---'*30)
    print('Aguarde enquanto o computador escolhe um número e fazemos a verificação')
    print('---'*30)
    sleep(1.5)
    if numero_usuario > numero_pc:
        print('Você errou, o número é menor. Tente novamente: ')
        contador_jogadas += 1
        numero_usuario = int(input('Digite um número de 1 a 10: '))
    elif numero_usuario < numero_pc:
        print('Você errou, o número é maior. Tente novamente: ')
        contador_jogadas += 1
        numero_usuario = int(input('Digite um número de 1 a 10: '))
    else:
        print(f'Parabéns, você precisou de {contador_jogadas} jogadas para ganhar!')
        opc = 0




