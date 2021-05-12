### Exercício Treino 1 - 
#           Escreva uma função que recebe dois parâmetros (números) e imprime o menor dos dois. 
#           Se eles forem iguais, imprima que são valores idênticos.

#input

numero1 = 100
numero2 = 20

#processamento
def verifica_menor_numero(numero1, numero2):
    if numero1 < numero2:
        return numero1
    elif numero1 == numero2:
        return 'números identicos'
    else:
        return numero2 

#output

#print(f'O menor número é: {verifica_menor_numero(numero1,numero2)}')

### Exercício Treino 2 - 
#           Escreva uma função que recebe dois números (a e b) como parâmetro 
#              e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.


def verificar_soma(numero_A, numero_B):
    limite = 100
    soma = numero_A + numero_B
    if soma > limite:
        return True
    else: 
        return False

#a = float(input('Digite um número: '))
#b = float(input('Digite outro número: '))

#print(verificar_soma(a, b))

### Exercício Treino 3 - 
#           Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas. 
#           Faça uma chamada à função, passando como parâmetro uma string



def tudo_minusculo(string):
    return string.lower()

#palavra = input('Digite uma palavra: ')

#print(tudo_minusculo(palavra))

###Exercício 4 - 
#   Crie um programa que tenha uma função chamada voto () que vai receber como parâmetro o ano de nascimento de uma pessoa, 
#       retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. 
#   Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.

def voto(ano_nascimento):
    import datetime as dt
    data_atual = dt.datetime.now()
    ano_atual = data_atual.year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return 'Negado'
    elif idade < 18:
        return 'Opcional'
    else:
        return 'Obrigatório'

#ano_de_nascimento = int(input('Digite o seu ano de nascimento (AAAA): '))
#print(voto(ano_de_nascimento))

### Exercício 5 - 
#           Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: 
#               o nome de um jogador e quantos gols ele marcou.
#           O programa deverá ser capaz de mostrar a ficha do jogador, 
#               mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador, gols):
    nome_jogador = jogador.capitalize()
    if gols <= 0:
        gols_jogador = 0
    else:
        gols_jogador = gols
    print(f'O nome do jogador é {nome_jogador} e fez {gols_jogador} gols!')

#jogador = input('Digite o nome do jogador: ')
#gols = int(input('Digite a quantidade de gols feitos: '))

#ficha(jogador, gols)



### Exercício 6 
#       Um professor, muito legal, fez 3 provas durante um semestre, 
#           mas só vai levar em conta as duas notas mais altas para calcular a média.
#       Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, 
#           a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.



def verificar_maior_nota(nota_1, nota_2, nota_3):
    if nota_1 > nota_2 and nota_1 > nota_1:
        return nota_1
    elif nota_2 > nota_1 and nota_2 > nota_3:
        return nota_2
    elif nota_3 > nota_1 and nota_3 > nota_2:
        return nota_3
    else:
        return nota_1

def verificar_menor_nota(nota_1, nota_2, nota_3):
    if nota_1 < nota_2 and nota_1 < nota_1:
        return nota_1
    elif nota_2 < nota_1 and nota_2 < nota_3:
        return nota_2
    elif nota_3 < nota_1 and nota_3 < nota_2:
        return nota_3
    else:
        return nota_1

def maiores_2_notas(n1, n2, n3):
    if verificar_menor_nota(nota_1, nota_2, nota_3) == n1:
        return (n2, n3)
    elif verificar_menor_nota(nota_1, nota_2, nota_3) == n2:
        return (n1, n3)
    elif verificar_menor_nota(nota_1, nota_2, nota_3) == n3:
        return (n1, n2)

def media_3_provas(nota_1, nota_2, nota_3):
    media = (nota_1 + nota_2 + nota_3) / 3
    return media

def media_2_maiores_notas(n1, n2):
    return (n1 + n2) / 2
    


    
nota_1 = 6
nota_2 = 8
nota_3 = 10
n1, n2 = maiores_2_notas(nota_1, nota_2, nota_3)

print(f'''A maior nota é: {verificar_maior_nota(nota_1, nota_2, nota_3)} 
e a menor é: {verificar_menor_nota(nota_1, nota_2,nota_3)}''')

print(f'''A média das tres notas é: {media_3_provas(nota_1, nota_2, nota_3)}
e a média das duas maiores notas é: {media_2_maiores_notas(n1, n2)} ''')