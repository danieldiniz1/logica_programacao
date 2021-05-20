#2.	Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] 
# e cada valor associado é o número ao quadrado.

numeros = list(range(1,11))
numeros_ao_quadrado = {}

for numero in numeros:
    numeros_ao_quadrado.update({numero : numero ** 2})

print(numeros_ao_quadrado)
