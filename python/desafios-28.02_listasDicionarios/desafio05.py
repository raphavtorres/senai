lista = []
lista_par = []
lista_impar = []
while True:
    num = float(input("Digite um valor: "))
    lista.append(num)

    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

    continuar = input("Deseja continuar? [S/N]: ").lower()
    if continuar != 's':
        break
print(f"Todos os valores: {lista}")
print(f"Valores par: {lista_par}")
print(f"Valores ímpares: {lista_impar}")
