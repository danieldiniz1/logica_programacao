# 1. Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas de um supermercado. 
# Não esqueça de fazer as seguintes validações:
# Produto Indisponível
# Produto Inválido
# Quantidade solicitada não disponível 
# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

produtos_disp = {'laranja' : [200, 0.15], 
                 'pera'    : [300, 0.5],
                 'uva'     : [250, 1.5] }

carrinho_produtos = []
carrinho_qtde = []

opc = 1
while opc == 1:  
    produto = input('Qual o nome do produto que deseja comprar:').lower().strip()
    while produto not in produtos_disp:
        print('Produto inválido, digite novamente:')
        produto = input('Qual o nome do produto que deseja comprar:').lower().strip()

    qtde = int(input('Qual a quantidade desejada(apenas valores inteiros, não vendemos partes):'))
    while qtde < 0:
        print('Quantidade inválida, digite novamente:')
        qtde = int(input('Qual a quantidade desejada(apenas valores inteiros, não vendemos partes):'))

    if produto not in produtos_disp:
        print('Produto Indisponível')
    
    if qtde > produtos_disp[produto][0]:
        print('Quantidade Solicitada Não Disponível')
        qtde = 0

    carrinho_produtos.append(produto)
    carrinho_qtde.append(qtde)      
    produtos_disp[produto][0] -= qtde

    resp = input('Deseja algo mais? [s/n]').lower().strip()
    while resp != 's' and resp != 'n':
        print('Operação inválida, digite novamente!')
        resp = input('Deseja algo mais? [s/n]').lower().strip()
    if resp == 'n':
        print('Segue abaixo sua conta:')
        opc = 0

total_valor = 0
for i, produto in enumerate(carrinho_produtos):
    if carrinho_qtde[i] == 0:
        pass
    else:
        valor = carrinho_qtde[i] * produtos_disp[produto][1]
        total_valor += valor
        print(f'Você comprou {carrinho_qtde[i]} {produto}s por R$ {valor:.2f}')

print(f'O total de itens foi de {sum(carrinho_qtde)} unidades')
print(f'O total da compra foi de R$ {total_valor}')