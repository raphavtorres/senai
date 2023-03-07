def escreva(msg):
    tam = len(msg)
    print("+" * tam)
    print(msg)
    print("+" * tam)


for i in range(3):
    msg = input(f"{i + 1}ª Mensagem: ")
    escreva(msg)
