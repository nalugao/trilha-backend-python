import os

restaurantes = [{'nome':'Mancini', 'categoria':'Italiano', 'ativo':False}, 
                {'nome':'Giraffas', 'categoria':'Brasileira', 'ativo':True},
                {'nome':'Son Sushi', 'categoria':'Japonês', 'ativo':False}]

def voltar_ao_menu():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite enter para voltar ao menu principal\n')
    main()

def exibir_nome_programa():
    print("""
        ╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
        ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
        ┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
        ╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
        ┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
        ╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
        ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
        ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
      """) # https://fsymbols.com/

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Finalizando app')

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Essa opção não é válida\n')

    voltar_ao_menu()

def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastro():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastrar restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante: ')

    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')

    dados_restaurate = {'nome': nome_restaurante,
                        'categoria':categoria, 
                        'ativo':False}
    
    restaurantes.append(dados_restaurate)

    print(f'O restaurante {nome_restaurante} foi adicionado com sucesso!')
    voltar_ao_menu()
    
def lista():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Lista de restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu()
    
def ativar_restaurante():
    exibir_subtitulo('Ativar restaurante')

    voltar_ao_menu()

def alterar_status_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''

    exibir_subtitulo('Alterando estado do restaurante:')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrato = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrato = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrato:
        print('O restaurante não foi encontrado.')
    
    voltar_ao_menu()

def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')
        
        if opcao_escolhida == 1:
            cadastro()
        elif opcao_escolhida == 2:
            lista()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
def main():
    ''' Função principal que inicia o programa '''
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()