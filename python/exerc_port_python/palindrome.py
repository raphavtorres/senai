import unicodedata

value = input("Type a message or a value to know if it's a palindrome: ").lower()

# treating the string
v_noesp = value.replace(" ", "")
v_formated = unicodedata.normalize("NFD", v_noesp)
v_formated = v_formated.encode("ascii", "ignore")
v_formated = v_formated.decode("utf-8")
print(v_formated)

if v_formated[::-1] == v_formated:
   print("\033[1;34;0 mPALINDROME!\033[m😎")
else:
   print("\033[1;31;0 mNOT A PALINDROME...\033[m😒")
