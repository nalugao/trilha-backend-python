"""Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro."""

atividade_A = int(input("Informe os dias para a atividade A: "))
atividade_B = int(input("Informe os dias para a atividade B: "))
atividade_C = int(input("Informe os dias para a atividade C: "))

if (atividade_A >= 0 and atividade_B >= 0 and atividade_C >= 0):
    tempo_total = atividade_A + atividade_B + atividade_C
    print(f"O tempo total do projeto é de {tempo_total} dias.")
else: 
    print("Erro: Os dias não podem ser negativos.")