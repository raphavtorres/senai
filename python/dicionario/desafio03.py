from datetime import date

ano_atual = date.today().year

print("-" * 20)

nome = input("Nome: ")
ano_nasc = int(input("Ano de nascimento: "))
cart_trab = input("Carteira de trabalho: ")

idade = ano_atual - ano_nasc

pessoa = {
    'nome': nome,
    'idade': idade,
    'cart_trab': cart_trab
}

if cart_trab != '0' and not len(cart_trab) <= 0:
    ano_contrat = int(input("Ano de contratação: "))
    salario = float(input("Salário: R$"))
    idade_aposent = ano_contrat - ano_nasc + 35

    pessoa['idade_aposent'] = idade_aposent
    pessoa['ano_contrat'] = ano_contrat
    pessoa['salario'] = salario


print("-" * 20)

print(f"Nome = {pessoa['nome']}")
print(f"Idade = {pessoa['idade']}")
print(f"CTPS = {pessoa['cart_trab']}")

if cart_trab != '0' and not len(cart_trab) <= 0:
    print(f"Ano de contratação = {pessoa['ano_contrat']}")
    print(f"Salário = {pessoa['salario']}")
    print(f"Aposentadoria = {pessoa['idade_aposent']}")

print(pessoa)
