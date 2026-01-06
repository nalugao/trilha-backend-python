"""Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres."""

def tamanho_palavra(palavra):
    return len(palavra)

conferencia_palavra = input('Digite uma palavra: ')
conferencia_tamanho = tamanho_palavra(conferencia_palavra)

print(f'Essa palavra tem {conferencia_tamanho} caracteres.')

#ou

def contar_caracteres(palavra): 
    return len(palavra) 
 
texto = input("Digite uma palavra: ") 
print(f"Essa palavra tem {contar_caracteres(texto)} caracteres.") 