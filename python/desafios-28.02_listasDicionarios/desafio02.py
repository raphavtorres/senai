def trabalharLista(list, num):
    if list.count(num) == 0:
        list.append(num)
        print("Sucesso!", end=' ')
    else:
        print("Valor já existente na lista!", end=' ')

    print(f"Lista = {list}")
    return list

list = []
while True:
    try:
        num = float(input("Digite o valor: "))
    except ValueError:
        print("Valor Inválido! Digite um número!")
        continue

    trabalharLista(list, num)

    continuar = input("Deseja continuar? [S/N]: ").lower().strip()
    if continuar != "s":
        print(f"Lista = {list.sort()}")
        break


