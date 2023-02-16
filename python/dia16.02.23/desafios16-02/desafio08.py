print("=====DESAFIO #08=====")

soma = 0
print("-" * 20)

for i in range(1, 7):
    num = int(input(f"Digite o {i}º valor: "))
    if num % 2 == 0:
        soma += num

print(f"Total: {soma}")

print("-" * 20)
