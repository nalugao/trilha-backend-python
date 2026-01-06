# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = {'nome':'Natalia',
          'idade':'25',
          'cidade':'São Paulo'}
print(pessoa)

# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
pessoa['idade'] = '26'
print(pessoa)

# Adicione um campo de profissão para essa pessoa;
pessoa['profissão'] = 'Engenheira de Software'
print(pessoa)

# Remova um item do dicionário.
pessoa.pop('cidade')
print(pessoa)

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
quadrados = {}
for n in range(1, 6):
    quadrados[n] = n**2

print(quadrados)

# numeros_quadrados = {x: x**2 for x in range(1, 6)}
# print(numeros_quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# if 'profissão' in pessoa:
#     print('A chave existe')
# else:
#     print('A chave não existe')

if 'cidade' in pessoa.keys():
    print('A chave existe')
else:
    print('A chave não existe')

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = "o rato roeu a roupa do rei de roma"
palavras = frase.split()

sequencia = {}

for palavra in palavras:
    if palavra in sequencia:
        sequencia[palavra] = sequencia[palavra] + 1  # ou +=1
    else:
        sequencia[palavra] = 1


print(sequencia)