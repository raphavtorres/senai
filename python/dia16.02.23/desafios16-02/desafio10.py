print("=====DESAFIO #10=====")

num = int(input("Digite um número: "))

divisores = 0

for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1
        print('\033[0;30;42m', i, '\033[m', end=' ')
    else:
        print('\033[0;30;41m', i, '\033[m', end=' ')
if divisores == 2:
    print("➡ É primo!")
else:
    print("➡ Não é primo!")
