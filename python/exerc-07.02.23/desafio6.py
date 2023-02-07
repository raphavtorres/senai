print("######### DESAFIO – 06 ##########")

name = input("Write a name: ").upper()

# MEU JEITO
list_alg = []
for alg in name:
    list_alg.append(alg)
    print(list_alg)

# JEITO BASEADO NO EXEMPLO PROF
# tam_nome = len(name)
# i = 1
# for alg in range(tam_nome):
#     print(name[0:i])
#     i += 1
