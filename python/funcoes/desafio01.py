print("-----CÁLCULO DE ÁREA-----")


def area(largura, comprimento):
    area = largura * comprimento
    return area


larg = float(input("Largura: "))
comp = float(input("Comprimento: "))
print(f"Área total = {area(larg, comp)}m²")
