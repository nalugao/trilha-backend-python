"""Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.

Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N."""

n = int(input("Digite um número: "))
def soma(numero):
    if numero == 0:
        return 0
    else:
        return numero + soma(numero - 1)

print(f"A soma é: {soma(n)}")