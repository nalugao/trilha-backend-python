# 1 - Crie uma lista para cada informação a seguir:
numeros = [1, 2, 'três', 4, 5, 'seis', 7, 8, 9, 10]
nomes = ['Natalia', 'Gloria', 'Marco', 'Tufão']
data_ano = [2000, 2026]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# for nome in nomes:
#     print(nome)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# soma_impares = 0

# for numero in numeros:
#     if numero %2 > 0:
#         soma_impares += numero
# print(soma_impares)
  
# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# for item in range(10, 0, -1):
#     print(item)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# numero = int(input('Digite um número: '))
# for n in range(1, 11):
#     print(f'{numero} x {n} = {numero*n}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# num = 0
# for n in numeros:
#     try:
#         num += n
#     except TypeError:
#         print(f'Erro: O elemento "{n}" não é um número válido e foi ignorado.')
# print(f'A soma total é: {num}')

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

