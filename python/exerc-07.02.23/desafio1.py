print("######### DESAFIO – 01 ##########")

full_name = input("Write your name: ")

upper = full_name.upper()
lower = full_name.lower()

amount_letters = len(full_name)

amount_spaces = full_name.count(" ")
amount_letters_nospaces = amount_letters - amount_spaces

name_list = full_name.split()

print(f"Uppercase: {upper}")
print(f"Lowercase: {lower}")
print(f"Amount of letters with spaces: {amount_letters}")
print(f"Amount of letters without spaces: {amount_letters_nospaces}")
print(f"Amount of letters in the first name: {name_list[0]}")
