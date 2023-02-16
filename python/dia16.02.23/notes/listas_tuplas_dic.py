listas = []  # imutável
tuples = ()
dicionario = {}  # chave valor

cores = {
    'Reprovado': '\33[30;41m',
    'Aprovado': '\33[30;44m',
    'Limpa': '\33[m'
}

media = float(input("Digite a média: "))
frequencia = float(input("Digite a frequência: "))

if media >= 50:
    r = 'Aprovado'
else:
    r = 'Reprovado'

print(f"Status: {r}\nMédia: {cores[r]}{media}{cores['Limpa']}")
