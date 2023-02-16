print("=====DESAFIO #13=====")

pesos = []


for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))
    pesos.append(peso)

maior = pesos[0]
menor = pesos[0]

for i in range(5):
    if maior < pesos[i]:
        maior = pesos[i]
    if menor > pesos[i]:
        menor = pesos[i]

print(f"Maior peso: {maior}")
print(f"Menor peso: {menor}")
