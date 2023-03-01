qnt_dig = 0
lista = []
while True:
    qnt_dig += 1

    num = float(input("Digite um valor: "))
    lista.append(num)

    lista_rev = lista[:]
    lista_rev.sort(reverse=True)

    continuar = input("Deseja continuar? [S/N]: ").lower()
    if continuar != 's':
        break

print(f"Quantidade de números que foram digitados = {qnt_dig}")
print(f"Valores em ordem decrescente = {lista_rev}")
