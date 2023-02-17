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
    print("O texto digitado \033[1;34;0 mÉ palindromo!\033[m")
else:
    print("O texto digitado \033[1;31;0 mNão é palindromo!\033[m")
