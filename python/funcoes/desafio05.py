from time import sleep
from random import randint

numeros = []


def sorteia():
    print("Sorteando: ", end=" ")
    for i in range(5):
        sleep(0.5)
        num_aleat = randint(0, 9)
        print(num_aleat, end=" ")
        numeros.append(num_aleat)
    print("")
    return numeros


def somaPar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma


print("-" * 20)
print(f"Lista de números sorteados {sorteia()}")
print(f"A soma dos pares sorteados é: {somaPar(numeros)}")
print("-" * 20)
