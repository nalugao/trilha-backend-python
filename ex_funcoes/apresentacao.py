#função simples com parâmetro
def ola_mundo(nome):
    return f"Olá, {nome}!"

print(ola_mundo("Natalia"))

#função closure, função dentro da função
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"
    return saudar

bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")
print(bom_dia('Vini'))
print(boa_noite('Ana'))

