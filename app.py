import os

restaurantes = [{"nome" : "Bar do Duh", "categoria" : "Bar", "ativo": True},
                {"nome" : "Espetinho do Vito", "categoria" : "Espetaria", "ativo": True},
                {"nome" : "Pastelaria do Rossi", "categoria" : "Pastelaria", "ativo": False},]

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
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}")
    restaurant_data =  {"nome":nome_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(restaurant_data)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    menu_principal()

def listar_restaurantes():
    subtitulo("Lista dos restaurantes")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f"-{nome_restaurante} | {categoria} | {ativo}")

    menu_principal()

def alterar_estado():
    subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: \n")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante["ativo"]
            mensagem = f'O restaurante{nome_restaurante} foi ativado com sucesso!' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado...')

    menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado()
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