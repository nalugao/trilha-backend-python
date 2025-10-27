# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
nomes = ["Natalia", "Marco", "Glória"]
anos = ["2000", "2025"]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# def lista():
#     for nome in nomes:
#         print(f"- {nome}")

# if __name__ == "__main__":
#     lista()

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# def somatoria():
#     soma = 0
#     for numero in numeros:
#         if numero % 2 != 0:
#             soma += numero
            
#     print(soma)

# if __name__ == "__main__":
#     somatoria()

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

def ordem_decrescente(numero):
    cont = 0
    for numero[-1] in range(numeros):
        print(cont)

if __name__ == "__main__":
    ordem_decrescente()