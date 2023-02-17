print("=====DESAFIO #06=====")

print("-" * 30)
soma = 0
for i in range(50 + 1):
    if (i % 2 != 0) and (i % 3 == 0):
        print(i, end=" ")
        soma += i

print("\n" + "-" * 30)

print(f"A soma dos ímpares multiplos de 3 é: {soma}")
