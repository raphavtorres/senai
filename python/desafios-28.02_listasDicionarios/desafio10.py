lista = \
    [
        [],
        [],
        []
    ]

total_pares = 0
total_impares = 0
print("-" * 20)
for linha in range(3):
    for coluna in range(3):
        num = float(input(f"Digite um valor para [{linha}][{coluna}]: "))
        if num % 2 == 0:
            total_pares += num
        else:
            total_impares += num

        lista[linha].append(num)

soma_terc_coluna = 0
for i in range(3):
    soma_terc_coluna += lista[i][2]

maior_seg_linha = max(lista[1])

print("-" * 20)
for i in range(3):
    print(lista[i])


print(f"Total Pares: {total_pares}")
print(f"Total Ímpares: {total_impares}")
print(f"Soma da 3ª coluna: {soma_terc_coluna}")
print(f"Maior valor da 2ª linha: {maior_seg_linha}")

