# 07 - Crie um programa onde o usuário possa digitar sete valores numéricos  e 
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares  em ordem crescente.

def recebe_verifica_numero():
    opc = 1
    numero = ''
    
    while opc ==1:
        try:
            numero = float(input('Digite um número: '))  
        except ValueError:
            print('Digite apenas números e tente novamente: ')
        
        if numero != '':
            opc = 0
        
    return(numero)

def verifica_par_impar(numero):
    if numero % 2 == 0:
        return('par')
    else:
        return('impar')

lista_numeros = []
pares = []
impares = []
qtde_numeros = int(input('Quantos números deseja verificar: '))

for valor in range(qtde_numeros):
    lista_numeros.append(recebe_verifica_numero()) 

for numero in lista_numeros:
    tipo = verifica_par_impar(numero)
    if tipo == 'par':
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort()

print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
    