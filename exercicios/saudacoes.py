def saudacoes(hora):
    if hora < 12:
        print("Bom dia!")
    elif hora < 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")

hora = int(input("Digite que horas são: \n"))
print(saudacoes(hora))