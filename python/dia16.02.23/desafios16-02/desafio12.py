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
print(f"Total de maiores: {maiores}")
print(f"Total de menores: {menores}")