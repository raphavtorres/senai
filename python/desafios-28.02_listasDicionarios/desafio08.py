lista = [[], []]

for i in range(7):
    num = float(input(f"Digite o {i + 1}º valor: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

pares = lista[0]
impares = lista[1]

pares.sort()
impares.sort()

print("-" * 20)
print(f"Todos os valores digitados: {lista}")
print(f"Pares em ordem crescente: {pares}")
print(f"Ímpares em ordem crescente: {impares}")