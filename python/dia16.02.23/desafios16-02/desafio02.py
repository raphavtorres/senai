print("=====DESAFIO #02=====")

num = int(input("Digite um número: "))
base = int(input('''Escolha uma das bases: 
[1] Binário
[2] Octal
[3] Hexadecimal'''))


def decBin():
    pass
# fundo amarelo


def decOct():
    pass
# fundo azul


def decHex():
    pass
# fundo rosa


if base == 1:
    decBin()
elif base == 2:
    decOct()
elif base == 3:
    decHex()
else:
    print("\33[31mOpção inválida.\33[m")

print(f"Sua opção: ")

