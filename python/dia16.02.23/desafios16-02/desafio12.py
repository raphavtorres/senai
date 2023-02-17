from datetime import date

print("=====DESAFIO #12=====")

ano_atual = date.today().year
maiores = 0
menores = 0

for i in range(1, 8):
    ano_nasc = int(input(f"Ano de nascimento da {i}ª pessoa: "))
    if (ano_atual - ano_nasc) >= 18:
        maiores += 1
    else:
        menores += 1

maiores = str(maiores)
print("Total de maiores: {}{}{}".format('\033[1;34m', maiores, '\033[m'))
print("Total de menores: {}{}{}".format('\033[1;31m', menores, '\033[m'))
