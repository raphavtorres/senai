print("######### DESAFIO – 04 ##########")
value = input("Write something: ")

# Tipo primitivo?
primitive = type(value)
# Só tem espaços?
space = value.isspace()
# É um número?
num = value.isnumeric()
# É alfabético?
alpha = value.isalpha()
# É alfanumérico?
alphanum = value.isalnum()
# Está em maiúsculas?
upper = value.isupper()
# Está em minúsculas?
lower = value.islower()
# Está capitalizada?
title = value.istitle()

print(f'Primitive type: {primitive}')
print(f'All spaces: {space}')
print(f'Number: {num}')
print(f'Alphabetic: {alpha}')
print(f'Alphanumeric: {alphanum}')
print(f'Upper case: {upper}')
print(f'Lower case: {lower}')
print(f'Title: {title}')