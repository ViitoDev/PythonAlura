import os

restaurantes = ["Pizzaria do Rossi","Caldinho do Du"]

def exibir_nome():
    print("Delivery App\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar resturante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    subtitulo("Encerrando o programa")

def menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal:\n")
    main()

def opcao_invalida():
    print("Opção inválida!\n")
    menu_principal()

def subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def cadastrar_restaurante():
    subtitulo("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar:\n")
    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    menu_principal()

def listar_restaurantes():
    subtitulo("Lista dos restaurantes")
    for restaurante in restaurantes:
        print(f"-{restaurante}")

    menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()