print("=====DESAFIO #02=====")

num = int(input("Digite um número: "))
base = int(input('''Escolha uma das bases: 
[1] Binário
[2] Octal
[3] Hexadecimal
Sua opção: '''))


def decBin():
    print(f"O binário de {num} é \033[0;30;43m{bin(num)}\033[m")
# fundo amarelo


def decOct():
    print(f"O octal de {num} é \033[0;30;44m{oct(num)}\033[m")
# fundo azul


def decHex():
    print("O hexadecimal de %d é \033[0;30;45m%04X\033[m" % (num, num))
# fundo rosa


if base == 1:
    decBin()
elif base == 2:
    decOct()
elif base == 3:
    decHex()
else:
    print("\33[31mOpção inválida.\33[m")
