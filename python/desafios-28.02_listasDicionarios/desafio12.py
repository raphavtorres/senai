cadastro = []
notas = []
i = 0
while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    notas.append(nota1)
    notas.append(nota2)

    cadastro.append(nome)
    cadastro.append(notas)

    continuar = input("Continuar? [S/N]: ").lower()
    if continuar != 's':
        print("INFORMAÇÕES FINAIS")
        break


print(cadastro)

print("Nº           Nome            Média")
i = 0
for pessoa in cadastro:
    print(i, pessoa[0], "----")
    i += 1

