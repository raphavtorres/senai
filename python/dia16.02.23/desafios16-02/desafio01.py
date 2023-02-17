print("=====DESAFIO #01=====")

valor_casa = float(input("Valor da casa: "))
sal = float(input("Salário: "))
anos = int(input("Por quantos anos vai pagar: "))

prest = valor_casa / (anos * 12)

print("-" * 30)
print("Valor da casa = R$ %.2f" % (valor_casa))
print("Salário = R$ %.2f" % (sal))
print("Prestação = R$ %.2f" % (prest))
if prest > (sal * 0.3):
    print("\033[1;30;41mEmpréstimo negado\033[m")
else:
    print("\033[1;30;42mLiberado\033[m")
