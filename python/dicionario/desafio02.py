from random import randint
from operator import itemgetter

jogos = {}
jogos_ord = {}

print("-" * 20)

for i in range(4):
    sorteado = randint(1, 6)
    jogos['Jogador' + str(i + 1)] = sorteado

    print(f"O Jogador{i + 1} sorteou {sorteado}")

print("-" * 20)
print(jogos)

jogos_ord = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print("-" * 20)

for i in range(4):
    print(f"O {i + 1}º lugar: {jogos_ord[i][0]} com {jogos_ord[i][1]}.")


