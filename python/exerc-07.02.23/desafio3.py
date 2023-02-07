print("######### DESAFIO – 03 ##########")

city_name = input("City's name: ").lower()
city_list = city_name.split()

is_santo = "santo" in city_list[0]

print(f"Stars with 'Santo': {is_santo}")
