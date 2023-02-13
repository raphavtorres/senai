a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

sqr_Bside = b ** 2
trapezoid = (a + b) * c / 2
cube = c ** 2 * 6

print(f"A) The square's area that the value B is the side: {sqr_Bside}")
print(f"B) The trapezoid's area that has A as short base, B as long base, C as height: {trapezoid}")
print(f"C) The cube's surface area with C as edge: {cube}")
