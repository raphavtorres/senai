# AINDA NÃO ESTÁ FUNCIONANDO

cadastro = []
lista_pesos = []

i = 0
while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))

    pessoa = [nome, peso]

    lista_pesos.append(pessoa[1])
    cadastro.append(pessoa)

    quit = input("Continuar? [S/N]: ").lower()
    if quit != 's':
        break

menor_peso = min(lista_pesos)
maior_peso = max(lista_pesos)


print(menor_peso, maior_peso)
print(cadastro)
# pessoa_menor_peso = cadastro.index(menor_peso)
# pessoa_maior_peso = cadastro.index(menor_peso)


print(f"Dados cadastrados: {cadastro}")
print(f"Total de cadastros: {len(cadastro)}")
# print(f"Maior peso: {pessoa_maior_peso}, com {maior_peso}Kg")
# print(f"Menor peso: {pessoa_menor_peso}, com {menor_peso}")

