ano_nasceu = int(input("Digite seu ano de nascimento: \n"))
ano_atual = int(input("Digite o ano atual: \n"))


def calcula_idade():
    idade = ano_atual - ano_nasceu
    print(f"Sua idade é: {idade}")

calcula_idade()