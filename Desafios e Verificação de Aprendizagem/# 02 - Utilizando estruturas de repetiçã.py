# 02 - Utilizando estruturas de repetição com variável de controle, 
# faça um programa que receba uma string com uma frase informada pelo usuário 
# e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela. 
# Depois mostre na tela essa mesma frase sem nenhuma vogal.
vogais = ['a', 'e', 'i', 'o', 'u']
frase = input('Digite uma frase: ')
contador = 0
lista_frase = list(frase)


for letra in frase:
    if letra in vogais:
        contador += 1
        lista_frase.remove(letra)

print(f'A frase continha {contador} vogais.')
print(f'Removendo as vogais, a frase fica assim: {lista_frase}')
