lista = []
expressao = input("Expressão: ")

for char in expressao:
    lista.append(char)

quant_par_esq = lista.count("(")
quant_par_dir = lista.count(")")

qnt_par = (quant_par_esq + quant_par_dir) // 2

is_valida = True

if quant_par_dir > 0 or quant_par_esq > 0:
    for i in range(qnt_par):
        if quant_par_esq != quant_par_dir or lista.index(")") < lista.index("("):
            is_valida = False
        lista.remove(")")
        lista.remove("(")


if is_valida:
    print("Expressão válida")
else:
    print("Expressão inválida")
