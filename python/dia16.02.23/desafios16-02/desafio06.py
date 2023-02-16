print("=====DESAFIO #06=====")

print("-" * 70)
soma = 0
for i in range(50 + 1):
    if i % 2 != 0:
        print(i, end=" ")
        soma += i

print("\n" + "-" * 70)

print(f"A soma dos ímpares é: {soma}")
