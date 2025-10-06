# def habilitacao():
#     idade = int(input('Qual sua idade? '))
#     tem_carteira = input('Tem carteira de habilitação? (s/n) ').lower() == 's'
    
#     if idade >= 18 and tem_carteira:
#         print('Pode dirigir')
#     else:
#         print('Não pode dirigir')
        
# habilitacao() 

def meia_entrada():
    idade = int(input('Qual sua idade?'))
    estudante = input('É estudante? (s/n)').lower() == 's'

    if idade >= 60 or estudante:
        print('Tem direito a desconto')
    else:
        print('Não tem direito a desconto')

meia_entrada()