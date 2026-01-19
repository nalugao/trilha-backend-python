"""João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago."""

def main():
    conta, gorjeta = read_input()


def read_input():
    conta = float(input("Digite o valor da conta: "))
    gorjeta = float(input("Digite a porcentagem de gorjeta: "))

    return conta, gorjeta

def calculate(float_conta, float_gorjeta):
    int_conta = int(float_conta * 100)
    int_gorjeta = int(float_gorjeta)

    


if __name__ == "__main__":
    main()