# def taxa_entrega():
    
#     entrega_km = int(input('Quantos km você andou? '))
#     if entrega_km < 5:
#         valor_entrega_km = 5
#     elif entrega_km < 10:
#         valor_entrega_km = 8
#     else:
#         valor_entrega_km = 10

#     chuva = input('Estava chovendo? (s/n) ').lower() == 's'
#     if chuva:
#         total_taxa = valor_entrega_km + 2
#         print(f'Valor a pagar: R$ {total_taxa:.2f}')
#     else:
#         print(f'Valor a pagar: R${valor_entrega_km:.2f}')

def getUserInput():
    entrega_km = int(input('Quantos km você andou? '))
    chuva = input('Estava chovendo? (s/n) ').lower() == 's'
    return entrega_km, chuva

def valorEntrega(entrega_km):
    if entrega_km < 5:
        valor = 5
    elif entrega_km < 10:
        valor = 8
    else:
        valor = 10
    return valor

def taxaChuva(chuva, valor):
    if chuva:
        valorTotal = valor + 2
        return valorTotal
    return valor

if __name__ == "__main__":
    km, choveu = getUserInput()
    valorBase = valorEntrega(km)
    pagamento = taxaChuva(choveu, valorBase)
    print(f'Valor a pagar: R$ {pagamento:.2f}')
