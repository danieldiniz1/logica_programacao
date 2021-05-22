# 04 - Utilizando funções e listas 
# faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato escrito por extenso. 
# Valide a data e retorne NULL caso a data seja inválida



def digitar_data():
    data = input('Digite uma data no formato DD/MM/AAAA: ').strip()
    return data

def verificar_mes_dia(dia, mes, ano):
    if dia > 31 or (dia > 30 and mes == 4) or (dia > 30 and mes == 6) or (dia > 30 and mes == 9) or (dia > 30 and mes == 11) or mes > 12 or ano < 1900:
        return True
    else:
        return False

def verificar_mes_fevereiro(dia, mes, ano):
    if ano % 4 == 0 and dia > 29 and mes == 2:
        return True
    elif dia > 28 and mes == 2 and ano % 4 != 0:
        return True
    else:
        return False

def verifica_caracteres_data(data):
    if len(data) != 10 or data[2] != '/' or data[5] != '/':
        return True
    else:
        return False

#            31          28         31       30       31      30       31      31        30          31          30           31         
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho','Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

data = digitar_data()
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[-4:])

while (verifica_caracteres_data(data) == True) or (verificar_mes_fevereiro(dia, mes, ano) == True) or verificar_mes_dia(dia, mes, ano) == True:
    print('Data inválida, digite novamente.')
    data = digitar_data()
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[-4:])
 
print(type(dia), mes, ano)
print(f'A data por extenso é dia: {data[0:2]} do mês de4 {meses[mes - 1]} do ano de {ano}. ')
