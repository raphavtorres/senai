# isinstance - to know if the object is of a certain type
# "tries the type to know if it is  instance of the class"
# note: Liskov Substitution Principle (LSP)
list = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'name': 'Raphael'}
]

for item in list:
    if isinstance(item, set):
        print('SET: \n')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print("STR: \n")
        print(item.upper(), isinstance(item, set))

    elif isinstance(item, (int, float)):
        print("NUM: \n")
        print(item, item * 2)

    else:
        print("Other: \n")
