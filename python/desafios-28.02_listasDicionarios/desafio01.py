list_num = []

i = 0
while i < 5:
    try:
        num = float(input(f"Digite o {i + 1}º número: "))
    except ValueError:
        print("VALOR INVÁLIDO! Digite um número!")
        continue
    list_num.append(num)
    i += 1

list_ord = list_num[:]
list_ord.sort()

ult_ind = len(list_num) - 1

maior_num = list_ord[ult_ind]
menor_num = list_ord[0]

pos_maior = list_num.index(maior_num)
pos_menor = list_num.index(menor_num)

print(f"Os números escolhidos foram: {list_num}")
print(f"O menor número é {menor_num} e está na {pos_menor + 1}ª posição . O maior é {maior_num} e está na {pos_maior + 1}ª posição")
