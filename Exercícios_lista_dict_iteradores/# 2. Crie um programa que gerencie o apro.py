#2.	Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feito em cada partida. 
# No final tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
cont_partidas = 1
cont_gols = []

nome_jogador = input('Digite o nome do jogador: ').capitalize().strip()
while nome_jogador.isalpha() is False:
    print('Nome Inválido, digite novamente') 
    nome_jogador = input('Digite o nome do jogador: ').capitalize().strip()
opc = 1
while opc == 1:
    gols = int(input(f'Digite a quantidade de gols marcados na {cont_partidas}º rodada: '))
    while gols < 0:
        print('Número Inválido, digite novamente!')
        gols = int(input(f'Digite a quantidade de gols marcados na {cont_partidas}º rodada: '))
    cont_partidas += 1
    cont_gols.append(gols)
    resp = input('Acabou as rodadas? [s/n]').lower().strip()
    while resp != 's' and resp != 'n':
        print('Resposta inválida, digite novamente!')
        resp = input('Acabou as rodadas? [s/n]').lower().strip()
    if resp == 's':
        print('-----'*15)
        print('Segue abaixo o resultado:')
        opc = 0
print(f'O jogador {nome_jogador} fez {sum(cont_gols)} gols no campeonato com {cont_partidas} partidas.')
resultado = {nome_jogador : cont_gols}
print(resultado)


