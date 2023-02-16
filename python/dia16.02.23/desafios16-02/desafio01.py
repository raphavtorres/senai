print("=====DESAFIO #01=====") #datetime #pintar primos de azul (% resto 0 por 1 e ele mesmo)

valor_casa = float(input("Valor da casa: "))
sal = float(input("Salário: "))
anos = int(input("Por quantos anos vai pagar: "))
prest_mensal = anos * 12
if prest_mensal > (sal * 0.3):
    print("Empréstimo negado")
else:
    print("Liberado")