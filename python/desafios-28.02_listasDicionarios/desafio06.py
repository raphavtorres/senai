lista = []
expressao = input("Expressão: ")

for char in expressao:
    lista.append(char)

quant_par_esq = lista.count("(")
quant_par_dir = lista.count(")")

if quant_par_esq != quant_par_dir or lista.index(")") < lista.index("("):
    print("Expressão inválida")
else:
    print("Expressão válida")
