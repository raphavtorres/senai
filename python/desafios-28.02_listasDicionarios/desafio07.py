qnt_pessoas = 0
cadastro = []

i = 0
while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))

    pessoa = [nome, peso]

    cadastro.append(pessoa)
    qnt_pessoas += 1

    quit = input("Continuar? [S/N]: ")
    i += 1
    if quit != 's':
        break
print(cadastro)
maior_peso = cadastro[0][1]
menor_peso = cadastro[0][1]
pessoa_maior_peso = cadastro[0][0]
pessoa_menor_peso = cadastro[0][0]

for p in cadastro:
    if maior_peso < p[1]:
        maior_peso = p[1]
        pessoa_maior_peso = p[0]

    if menor_peso > p[1]:
        menor_peso = p[1]
        pessoa_menor_peso = p[0]

print(f"Dados cadastrados: {cadastro}")
print(f"Total de cadastros: {qnt_pessoas}")
print(f"Maior peso: {pessoa_maior_peso} com {maior_peso}Kg")
print(f"Menor peso: {pessoa_menor_peso} com {menor_peso}Kg")
