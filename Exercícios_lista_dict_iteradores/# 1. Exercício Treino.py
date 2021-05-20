# 1.	Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) 
# e seus valores correspondentes aos quadrados desses números.
#{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}  

numeros = [1, 4, 5, 6, 7, 9]
dicionario = {}

for numero in numeros:
    dicionario.update({numero : numero ** 2})

print(dicionario)
