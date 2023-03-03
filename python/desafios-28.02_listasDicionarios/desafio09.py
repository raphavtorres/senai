lista = [[], [], []]

print("-" * 20)
for coluna in range(3):
    for linha in range(3):
        num = float(input(f"Digite um valor para [{coluna}][{linha}]: "))
        lista[coluna].append(num)

print("-" * 20)
for i in range(3):
    print(lista[i])