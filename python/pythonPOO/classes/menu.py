cadastro = []
clientes = []
novo_usuario = []
planos = ["basic", "medium", "premium"]
filmes = [
    ['Homem-Aranha'],
    ['Homens de Preto'],
    ['Interestelar'],
    ['Shrek'],
    ['Gato de Botas'],
    []
]

def menu():
    while True:
        print(""
              "[0] - Sair\n"
              "[1] - Cadastrar\n"
              "[2] - Entrar\n"
              "[3] - Registrar Filme\n"
              "[4] - Listar Filmes")
        op = int(input("Escolha a opção: "))

        if op == 0:
            break
        elif op == 1:
            cadastrar_usuario()
        elif op == 2:
            entrar()
        elif op == 3:
            registrar_filme()
        elif op == 4:
            print(filmes)


def cadastrar_usuario():
    cadastro.append(input("Nome: "))
    cadastro.append(input("Email: "))
    print("Planos: | basic | medium | premium |")
    while True:
        plano = input("Plano: ").lower().strip()
        if plano in planos:
            break
        else:
            print("Plano inválido\n digite um plano válido \n Planos: | basic | medium | premium |  ")
    cadastro.append(plano)
    clientes.append(cadastro[:])
    cadastro.clear()
    print(clientes)


def entrar():
    while True:
        cliente = input('Nome: ')
        for i in range(len(clientes)):
            if cliente == clientes[i][0]:
                novo_usuario.append(clientes[i][0])
                novo_usuario.append(clientes[i][1])
                novo_usuario.append(clientes[i][2])
                break

            print("Cliente não cadastrado")


def registrar_filme():
    while True:
        filme = []
        nome_filme = input("Nome do filme: ")
        filme.append(nome_filme)

        plano_filme = input("Plano do filme: ").lower()
        filme.append(plano_filme)

        if plano_filme in planos:
            filmes.append(filme)
            continuar = input('Deseja continuar? [S/N]: ').lower()
            if continuar != 's':
                break
        else:
            print("Plano inexistente")
    print(filmes)
