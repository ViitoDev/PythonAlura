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
    os.system("cls")
    print("Encerrando o programa\n")

def opcao_invalida():
    print("Opção inválida!\n")
    input("Digite uma tecla para voltar ao menu principal:\n")
    main()

def cadastrar_restaurante():
    os.system("cls")
    print("Cadastro de novos restaurantes")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar:\n")
    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    input("Digite uma tecla para voltar ao menu principal\n")
    main()

def listar_restaurantes():
    os.system("cls")
    print("Lista dos restaurantes\n")

    for restaurante in restaurantes:
        print(f"-{restaurante}")

    input("\nDigite uma tecla para voltar ao menu principal\n")
    main()

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