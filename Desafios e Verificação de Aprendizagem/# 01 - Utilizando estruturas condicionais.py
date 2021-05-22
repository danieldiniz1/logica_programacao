# 01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
#•	A soma deles;
#•	A multiplicação entre eles;
#•	A divisão  inteira deles;
#•	Mostre na tela qual é o maior;
#•	Verifique se o resultado da soma é par ou ímpar e mostre na tela;
#•	Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

num_1 = float(input('Digite o valor do primeiro número: '))
num_2 = float(input('Digite o valor do segundo número: '))
soma = num_1 + num_2
multi_num = num_1 * num_2
divi_num = num_1 / num_2
if num_1 > num_2:
    maior = num_1
else:
    maior = num_2

if soma % 2 == 0:
    tipo_num = 'Par'
else:
    tipo_num = 'Ímpar'

if multi_num > 40:
    inteiro  = multi_num / (num_1 // num_2)
else:
    inteiro = 'resultado menor que 40!'
print('-----'*30)
print(f'A soma dos numeros {num_1} e {num_2} é: {soma:.2f}')
print('-----'*30)
print(f'A multiplicação dos numeros {num_1} e {num_2} é: {multi_num:.2f}')

print('-----'*30)
print(f'A divisão dos numeros {num_1} e {num_2} é: {divi_num:.2f}')
print('-----'*30)
print(f'O maior numero dos numeros {num_1} e {num_2} é: {maior}')
print('-----'*30)
print(f'O resultado da operação dos numeros {num_1} e {num_2} é : {inteiro}')
