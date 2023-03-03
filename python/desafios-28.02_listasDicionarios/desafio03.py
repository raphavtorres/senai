lista = []
lista_ord = []
num_menor = 0

for i in range(5):
    num = float(input(f"Digite o {i + 1}º número: "))
    lista.append(num)

for i in range(5):
    menor = min(lista)
    lista_ord.append(menor)
    lista.remove(menor)


print(lista_ord)