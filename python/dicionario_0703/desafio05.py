lista_pessoas = []

while True:
    nome = input("Nome: ")

    # TESTANDO ENTRADE DE SEXO
    while True:
        sexo = input("Sexo [M/F]: ").lower()
        if sexo != 'm' and sexo != 'f':
            print('Valor inválido para SEXO!')
            continue
        else:
            if sexo == 'm' or sexo == 'f':
                break

    idade = int(input("Idade: "))

    dic_pessoa = {
        'nome': nome,
        'sexo': sexo,
        'idade': idade
    }

    lista_pessoas.append(dic_pessoa)

    quit = input("Deseja continuar? [S/N]: ").lower()
    if quit != 's':
        break

qnt_cadastrados = len(lista_pessoas)

soma_idades = 0
mulheres = ''
for pessoa in lista_pessoas:
    soma_idades += pessoa['idade']
    if pessoa['sexo'] == 'f':
        mulheres += (pessoa['nome'] + ' ')

media_idades = round(soma_idades / qnt_cadastrados, 1)

print("-" * 40)
print(f"Total de pessoas cadastradas é {qnt_cadastrados}.")
print("-" * 40)

print(f"A média das idades é {media_idades} anos.")
print("-" * 40)

print(f"Mulheres cadastradas: {mulheres}")
print("-" * 40)

print("Pessoas com idade acima da média:")

for i in range(len(lista_pessoas)):
    if lista_pessoas[i]['idade'] > media_idades:
        print(f"nome={lista_pessoas[i]['nome']}\tsexo={lista_pessoas[i]['sexo'].upper()}\tidade={lista_pessoas[i]['idade']}")


print("-" * 40)
