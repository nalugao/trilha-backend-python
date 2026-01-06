#Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

limite = 3000.00
total_despesas = float(input('Digite o total de despesas do mês (R$): '))

if total_despesas > limite:
    print('Atenção! Você ultrapassou o limite do orçamento.')
else:
    print('Você está dentro do orçamento.')