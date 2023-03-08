todos_jogadores = []

while True:
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

    todos_jogadores.append(info_jogador)

    # PERGUNTANDO SE USUÁRIO QUER FINALIZAR
    continuar = True
    while True:
        quit = input("Deseja continuar? [S/N]: ").lower()
        if quit != 's' and quit != 'n':
            print('ERROR! Digite apenas "S" ou "N".')
            continue
        else:
            if quit == 's':
                break
            else:
                continuar = False
                break
    if not continuar:
        break

print("-" * 40)

# APRESENTANDO STATUS JOGADORES
for i, jogador in enumerate(todos_jogadores):
    print(f"{i + 1}º {jogador['nome']}\t{jogador['gols']}\ttotal: {jogador['total']}")

print("-" * 40)

while True:
    id_jogador = int(input("Digite o número do jogador para resumir ou 999: "))
    if id_jogador == 999:
        break
    else:
        jogador_por_id = todos_jogadores[id_jogador - 1]
        print(f"------- JOGADOR {jogador_por_id['nome']} -------")

        for i in range(jogador_por_id['num_partidas']):
            print(f"Na partida {i + 1}, o jogador {jogador_por_id['nome']} fez {jogador_por_id['gols'][i]} gols.")

        print("-" * 40)
