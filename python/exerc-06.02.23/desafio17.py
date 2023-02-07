import math

print("######### DESAFIO – 17 ##########")
# não encontrei uma boa tradução para cateto oposto e adjacente então fiz esse em português

cateto_oposto = float(input("Cateto Oposto: "))
cateto_adjacente = float(input("Cateto Adjacente: "))

hipotenusa = round((cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2), 2)
print(f"O comprimento da hipotenusa é {hipotenusa}")
