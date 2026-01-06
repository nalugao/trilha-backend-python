# def conversorMoeda():
#     valor = int(input('Qual o valor em reais você quer converter para Dólar? '))
#     taxa_atual = int(input('Qual a taxa atual?'))
#     dolar = valor * taxa_atual
#     print(f'O valor total em Dólar é de US${dolar:.2f}')

def getUserInput():
    valor = int(input('Qual o valor em reais você quer converter para Dólar? '))
    taxa_atual = float(input('Qual a taxa atual? '))

    return valor, taxa_atual

def conversorMoeda(valor, taxa_cambio):
    return valor * taxa_cambio

if __name__ == "__main__":
    x, y = getUserInput()
    convertido = conversorMoeda(x, y)
    print(f'O valor total convertido é de {convertido:.2f}')
