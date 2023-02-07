print("######### DESAFIO – 04 ##########")
# MEU JEITO
name = input("Write a name: ").upper()

list_alg = []
for alg in name:
    list_alg.append(alg)

list_alg.reverse()

print(list_alg)


#JEITO PROF
# name = input("Write a name: ").upper()
# name_invert = name[::-1]
#
# print(name_invert)
