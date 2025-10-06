def getUserInput():
    qtd_item = int(input('Quantidade: '))
    cadastrado = input('Cadastro? (s/n) ').lower() == 's'
    return qtd_item, cadastrado

def caracteristicas(qtd_item):
    total = 0
    cont = 0
    while cont < qtd_item:
       nome = input('Nome: ')
       preco = int(input('Preço: '))
       total = total + preco
       cont = cont + 1
    return total

def cadastro(cadastrado, total):
    if cadastrado:
        desconto = total * 0.10
        valorFinal = total - desconto
        return valorFinal
    return total

if __name__ == '__main__':
    qtd, cadastroAtivo = getUserInput()
    preco = caracteristicas(qtd)
    pagamento = cadastro(cadastroAtivo, preco)
    print(f'O valor a pagar R${pagamento:.2f}')