"""Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno."""

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

print(f"\nSua média foi: {media:2f}\n")

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")