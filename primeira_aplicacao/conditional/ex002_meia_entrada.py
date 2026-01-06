# def meia_entrada():
#     idade = int(input('Qual sua idade? '))
#     estudante = input('Você é estudante? (s/n) ').lower() == 's'
#     preco = 40

#     if idade < 18 or estudante:
#         preco_meia = preco/2
#         print(f'Você tem direito a meia-entrada e pagará R${preco_meia:.2f}.')
#     else:
#         print(f'Você NÃO tem direito a meia-entrada e pagará R${preco:.2f}.')

def getUserInput():
    idade = int(input('Idade: '))
    estudante = input('Estudante ? (s/n) ').lower() == 's'
    valor = 40
    return idade, estudante, valor

def meia_entrada(idade, estudante, valor):
    if idade < 18 or idade >= 60 or estudante:
        preco_meia = valor / 2
        return preco_meia
    return valor

if __name__ == "__main__":
    x, y, z = getUserInput()
    pagamento = meia_entrada(x, y, z)
    print(f'O valor a pagar é: R$ {pagamento:.2f}')