from datetime import date

print("=====DESAFIO #03=====")

ano_atual = date.today().year

ano_nasc = int(input("Ano de Nascimento: "))
idade = ano_atual - ano_nasc

if idade < 18:
    print(f"Falta(m) {18 - idade} ano(s) para se alistar")
elif idade == 18:
    print("Hora de se alistar")
else:
    print(f"Passou do tempo faz(em) {idade - 18} ano(s)")
