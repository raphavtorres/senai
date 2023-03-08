nome_jogador = input("Nome do Jogador: ")
num_partidas = int(input("Número de partidas: "))

todos_gols = []
total_gols_camp = 0

for i in range(num_partidas):
    gols = int(input(f"Gols na partida {i + 1}ª: "))
    todos_gols.append(gols)
    total_gols_camp += gols


info_jogador = {
    "nome": nome_jogador,
    "num_partidas": num_partidas,
    "gols": todos_gols,
    "total": total_gols_camp
}

print("-" * 20)
print(info_jogador)
print("-" * 20)

print(f"O campo nome tem valor {info_jogador['nome']}.")
print(f"O campo gols tem valor {info_jogador['gols']}.")
print(f"O campo total tem valor {info_jogador['total']}.")
print("-" * 20)

print(f"O jogador {info_jogador['nome']} \
jogou {info_jogador['num_partidas']} partidas.")

print("-" * 20)

for i in range(num_partidas):
    print(f"Na partida {i + 1}, fez {info_jogador['gols'][i]} gols.")
