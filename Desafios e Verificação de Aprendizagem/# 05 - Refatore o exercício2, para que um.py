#05 - Refatore o exercício2, para que uma função receba a frase, 
# faça todo o tratamento necessário e retorne o resultado. 
# Depois mostre na tela o resultado e a quantidade de letras que foram retiradas da frase original.
frase = input('Digite uma frase: ')

def contar_vogais(frase):
    vogais = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    lista_frase = list(frase)

    for letra in frase:
        if letra in vogais:
            contador += 1
            lista_frase.remove(letra)
    return(contador, lista_frase)

qtde, nova_frase = contar_vogais(frase)

print(f'A frase continha {qtde} vogais.')
print(f'Removendo as vogais, a frase fica assim: {nova_frase}')