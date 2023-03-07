nome = input("Aluno: ")
nota = float(input(f"Nota de {nome}: "))

aluno = {
    'nome': nome,
    'nota': nota
}

print(aluno)

print(f"Nome do aluno é {aluno['nome']}, e sua nota é {aluno['nota']}")

if aluno['nota'] <= 3.9:
    print('Reprovado')
elif aluno['nota'] <= 6.9:
    print("Recuperação")
elif aluno['nota'] <= 10:
    print("Aprovado")
else:
    print("Valor de nota inválido")
    