import os

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
    input("Digite uma tecla para voltar ao menu principal")
    main()

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))
    if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print("Listar restaurantes")
    elif opcao_escolhida == 3:
        print("Ativar restaurante")
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        opcao_invalida()

def main():
    os.system("cls")
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()