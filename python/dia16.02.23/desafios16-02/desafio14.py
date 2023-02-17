print("=====DESAFIO #14=====")

lista = []

idade = 0
idade_velho = 0
m_nova = 0
media_id = 0

for i in range(1, 5):
    print(f"----- {i}ª Pessoa -----")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo(M/F): ").upper()

    dic = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo
    }

    media_id += dic["idade"]

    if (dic["sexo"] == "M") and (idade_velho < dic["idade"]):
        idade_velho = dic["idade"]
        nome_velho = dic["nome"]

    if (dic["sexo"] == "F") and (dic["idade"] < 20):
        m_nova += 1

media_id /= 4

print("-" * 30)
print(f"Média de idade: {media_id}")
print(f"Nome do homem mais velho: {nome_velho}")
print(f"Quantidade de mulheres abaixo de 20 anos = {m_nova}")
print("-" * 30)
