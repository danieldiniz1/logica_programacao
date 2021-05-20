#4.	Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, 
# sabendo que o vencedor tirou o maior número no dado. 
# Dicas: procure sobre a função randint(), sleep() e itemgetter da bliblioteca operator.

import random 
import time

jog_1 = random.randint(1,6)
jog_2 = random.randint(1,6)
jog_3 = random.randint(1,6)
jog_4 = random.randint(1,6)

resultados = {'Jogador 1' : jog_1, 'jogador 2' : jog_2, 'Jogador 3' : jog_3, 'jogador 4' : jog_4}
for i, jogador in enumerate(resultados):
    print(f'O jogador {i + 1} tirou {resultados[jogador]} no dado!')
    time.sleep(2)


resutlados_ordenados = {}
for jogador in sorted(resultados, key = resultados.get, reverse = True):
    resutlados_ordenados.update({jogador : resultados[jogador]})
print(' -- RESULTADOS -- ')
for i, jogador in enumerate(resutlados_ordenados):
    print(f'Em {i + 1}º ficou o {jogador} com valor de {resutlados_ordenados[jogador]}!')
    time.sleep(2)

print('---'*15)
print(resutlados_ordenados)