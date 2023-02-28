list_num = []

i = 0
while i < 5:
   try:
       num = float(input(f"Digite o {i + 1}º número: "))
   except Exception:
       print("VALOR INVÁLIDO! Digite um número!")
       continue
   list_num.append(num)
   i += 1

list_ord = list_num[:]
list_ord.sort()

ult_ind = len(list_num) - 1

maior_num = list_ord[ult_ind]
menor_num = list_ord[0]

print(f"Os números escolhidos foram: {list_num}")
print(f"O menor número é {menor_num} e o maior é {maior_num}")
