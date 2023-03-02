from random import randint

lista = []

qnt_jogos = int(input("Quantos jogos você deseja gerar?: "))
print("-" * 5, f"Sorteando {qnt_jogos} jogos", "-" * 5)

for i in range(qnt_jogos):
    lista_jogo = []
    for j in range(6):
        lista_jogo.append(randint(1, 60))
    lista.append(lista_jogo)
    print(f"Jogo {i + 1}: {lista[i]}")
