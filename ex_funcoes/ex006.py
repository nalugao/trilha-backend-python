"""Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
"""

"""A sintaxe da função filter é:

filter(funcao, iteravel) 

Nela:

funcao é a função de filtragem dos elementos, que deve retornar True ou False; 
e iteravel é a estrutura na qual a função funcao será aplicada.
"""

numeros = input("Digite os números separados por espaço: ").split()

def conversor_numeros_inteiros(lista):
    lista_inteiros = []
    for numero in lista:
        lista_inteiros.append(int(numero))
    return lista_inteiros

def separador_numeros_pares(numero):
    return numero % 2 == 0

lista = conversor_numeros_inteiros(numeros)

print(list(filter(separador_numeros_pares, lista)))

#ou

numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) 
print("Números pares:", " ".join(pares)) 