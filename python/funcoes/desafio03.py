def contador(inicio, fim, passo):
    if fim < inicio:
        passo *= -1

    for i in range(inicio, fim + 1, passo):
        print(i, end="|")


for i in range(1, 11):
    print(i, end="|")
print("")

for i in range(10, -1, -2):
    print(i, end="|")
print("")

inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

contador(inicio, fim, passo)
