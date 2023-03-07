def maior(numeros):
    maior = 0
    for num in numeros:
        if num > maior:
            maior = num

    print("Analisando os valores")
    print(numeros)
    print(f"Maior valor = {maior}")


numeros = []
while True:
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)
    quit = input("Continuar? [S/N]: ").lower()
    if quit != 's':
        maior(numeros)
        break
