"""Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.

Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário."""


valor_desconto = float(input("Digite a porcentagem de desconto: "))
valor_conta = float(input("Digite o valor da compra: "))

def calculo_conta(desconto):
    def preco_conta(preco):
        total = preco - ((preco * desconto) / 100)
        return total
    return preco_conta

desconto = calculo_conta(valor_desconto)

print(f"Preço final com desconto: {desconto(valor_conta)}")