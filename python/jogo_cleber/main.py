from random import randint
import time

# sortear valor de 1 a 100
n_sorteado = randint(1, 100)

# Começa com 50 de vida
vida = 50


# 3 tentativas
tentativa = 1
while tentativa <= 3:

    print(f"Quantidade de vida: {vida}")
    n_user = int(input(f"Digite seu {tentativa} palpite: "))

    if n_user != n_sorteado:
        perde_vida = abs(n_sorteado - n_user)
        vida -= perde_vida
        if vida <= 0:
            print("VOCÊ PERDEU! Acabaram suas vidas...")
            break
    else:
        print("Parabéns, você ganhou!")
        break
    tentativa += 1

if vida > 0 and n_user != n_sorteado:
    print("VOCÊ PERDEU! Acabaram suas tentativas...")

# tempo de jogo = 60 seg ((time ou datetime))
# criar função para cada ação

