day_current = int(input("Current day: "))
month_current = int(input("Current month: "))
year_current = int(input("Current Year: "))

day_birth = int(input("Day you were born: "))
month_birth = int(input("Month you were born: "))
year_birth = int(input("Year you were born: "))

if year_current - year_birth < 18:
    print("You can't get a driver's license!")
elif month_current < month_birth:
    print("You can't get a driver's license!")
elif day_current < day_birth:
    print("You can't get a driver's license!")
else:
    print("You can get a drive's license!")


