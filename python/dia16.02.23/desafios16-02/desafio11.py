import unicodedata

print("=====DESAFIO #11=====")

value = input("Escreva uma frase para testar se é palíndromo: ").lower()

# tratando a string
v_noesp = value.replace(" ", "")
v_formatado = unicodedata.normalize("NFD", v_noesp)
v_formatado = v_formatado.encode("ascii", "ignore")
v_formatado = v_formatado.decode("utf-8")
print(v_formatado)

# ARRUMAR CORES
if v_formatado[::-1] == v_formatado:
    print("\33[1; 34mÉ palindromo! ")
else:
    print("\33[1; 31mNão é palindromo!")
