"""Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente."""

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operador = input("Escolha a operação (| + | - | * | / |): ")

if operador == "+":
    soma = lambda a, b: a + b
    print(f"O resultado é: {soma(n1, n2)}")
elif operador == "-":
    subtracao = lambda a, b: a - b
    print(f"O resultado é: {subtracao(n1, n2)}")
elif operador == "*":
    multiplicacao = lambda a, b: a * b
    print(f"O resultado é: {multiplicacao(n1, n2)}")
elif operador == "/":
    if n2 == 0:
        print("Erro: Não é possível dividir por zero!")
    else:
        divisao = lambda a, b: a / b
        print(f"O resultado é: {divisao(n1, n2)}")
else:
    print("Operador inválido! Use +, -, * ou /")


#ou


# operacoes = { 
#     '+': soma,  
#    '-': subtrai, 
#     '*': multiplica, 
#     '/': divide 
# } 

# if operacao in operacoes:  
#    resultado = operacoes[operacao](x, y)  
#    print(f"O resultado é: {resultado}")  
# else:  
#    print("Operação inválida") 