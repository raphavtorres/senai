qnt_dig = 0
lista = []
is_in_lista = True

while True:
    qnt_dig += 1

    num = float(input("Digite um valor: "))
    lista.append(num)

    lista_rev = lista[:]
    lista_rev.sort(reverse=True)

    continuar = input("Deseja continuar? [S/N]: ").lower()
    if continuar != 's':
        break

if lista.count(5) > 0:
    print("5 está em lista")
else:
    print("5 não está em lista")

print(f"Quantidade de números que foram digitados = {qnt_dig}")
print(f"Valores em ordem decrescente = {lista_rev}")
