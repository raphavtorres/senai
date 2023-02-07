print("######### DESAFIO – 05 ##########")

name = input("Write a name: ").upper()

list_alg = []
for alg in name:
    list_alg.append(alg)

while len(list_alg) != 0:
    print(list_alg)
    list_alg.pop()
