import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():

    print("""
        
    ╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
    ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
    ┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
    ╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
    ┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
    ╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
        """) #fsymbols.com

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def voltar_menu():
    input('\nDigite uma tecla apra voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastros de novos restaurantes')
    nome_restaurante = input('Nome: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()

def lista_restaurantes():
    exibir_subtitulo('Lista dos restaurantes')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    voltar_menu()

def finalizar_app():
    exibir_subtitulo('Encerrando programa')

def opcao_invalida():
    print('Opção inválida\n')
    voltar_menu()

try:
    def escolha_opcoes():
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            lista_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
except:
    opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolha_opcoes()

if __name__ == "__main__":
    main()