print("######### DESAFIO – 15 ##########")

kilometers = float(input("Kilometers traveled: "))
days = int(input("Days rented: "))

pay = (days * 60) + (kilometers * 0.15)

print(f"You need to pay R$ {pay:.2f}")
