num = int(input("Write a integer number: "))

num_static = num
fat = num
print(f"{num}! = 5", end="")
while num > 1:
    fat *= (num - 1)
    print(" * " + str(num - 1), end="")
    num -= 1

print(f"\n{num_static}! = {fat}")
