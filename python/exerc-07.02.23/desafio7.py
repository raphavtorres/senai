print("######### DESAFIO – 07 ##########")

phone = input("Write your cellphone number: ")

if len(phone) < 8:
    print("Invalid Number")
    exit()

phone = phone.split('-')

number_format = []
for part in phone:
    number_format += part

if len(number_format) < 9:
    number_format.insert(0, "9")

number = ""
for alg in number_format:
    number += alg

print(number)
