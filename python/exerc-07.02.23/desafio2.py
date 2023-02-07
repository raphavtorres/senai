print("######### DESAFIO – 02 ##########")

number_str = input("Write a number: ")
if int(number_str) < 1000 or int(number_str) > 9999:
    print("Invalid Number. Needs to be between 1000 and 9999")
    exit()

list_alg = []
for alg in number_str:
    list_alg.append(alg)

# print(list_alg)

print(f"Unit: {list_alg[3]}")
print(f"Ten: {list_alg[2]}")
print(f"Hundred: {list_alg[1]}")
print(f"Thousand: {list_alg[0]}")
