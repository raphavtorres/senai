print("=====DESAFIO #10=====")
#pintar primos de azul (% resto 0 por 1 e ele mesmo)

#AINDA NÃO CONSEGUI FAZER O PRIMO

num = int(input("Digite um número: "))

primo = 0
for i in range(1, num + 1):
    if (num % (i + 1) != 0) and (i != num):
        primo += 1

    print(i, end=' ')

if primo > 1:
    print("É primo!")

