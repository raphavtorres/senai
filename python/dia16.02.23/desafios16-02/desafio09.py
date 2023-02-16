print("=====DESAFIO #09=====")

print("-" * 30)

p_termo = int(input("Primeiro termo: "))
r = int(input("Razão: "))

for i in range(10):
    print(p_termo, end=' ')
    p_termo += r

print("\n" + "-" * 30)
