cadastro = []
notas = []

while True:
    nome = input("Digite o nome do aluno: ")
    try:
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
    except ValueError:
        print("Valor inválido! Digite apenas número.")
        continue

    if nota1 > 10 or nota2 > 10 \
            or nota1 < 0 or nota2 < 0:
        print("Valor Inválido! Nota máxima deve ser 10.")
        continue

    notas.append(nota1)
    notas.append(nota2)

    pessoa = [nome, notas]

    cadastro.append(pessoa)

    notas = []

    quit = input("Continuar? [S/N]: ").lower()
    if quit != 's':
        print(f"Nº\tNome\t\tMédia")
        break
print(cadastro)

print("-" * 20)
for aluno in cadastro:
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(f"{cadastro.index(aluno) + 1}\t{aluno[0]}\t\t{media}")
print("-" * 20)

while True:
    cod_aluno = int(input("Digite o número de um aluno ou 999 para sair: "))
    if cod_aluno == 999:
        break
    elif cod_aluno <= 0 or cod_aluno > len(cadastro):
        print("Código de aluno INVÁLIDO ou INEXISTENTE...")
        continue
    nome_aluno_esc = cadastro[cod_aluno - 1][0]
    nota_aluno_esc = cadastro[cod_aluno - 1][1]
    print(f"Notas de {nome_aluno_esc}: {nota_aluno_esc}")

