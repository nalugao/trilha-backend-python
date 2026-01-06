#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

try:
    maça = int(input('digite a quantidade de maçãs vendidas: '))
    banana = int(input('digite a quantidade de bananas vendidas: '))


    if maça > banana:
        print('As maçãs tiveram mais vendas')
    elif maça == banana:
        print('As vendas de bananas e maçãs foram as mesmas')
    else:
        print('As bananas tiveram mais vendas')

except ValueError:
    print('Digite apenas números')