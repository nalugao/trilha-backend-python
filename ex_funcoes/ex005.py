"""Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total."""

vendas = input("Digite os valores das vendas: ")

def separador_vendas(lista):
    return lista.split()

def conversor(vendas):
    return [int(venda) for venda in vendas] 

def somador_vendas(lista_vendas):
    total_vendas = sum(lista_vendas)

    print(f"O total de vendas é {total_vendas}")

lista_separada = separador_vendas(vendas)
lista_inteiros = conversor(lista_separada)
total = somador_vendas(lista_inteiros) 
print(f"O total de vendas é {total}")

#ou

valores = input("Digite os valores das vendas: ").split() 
total = sum(map(float, valores)) 
print(f"O total de vendas foi: {total}") 