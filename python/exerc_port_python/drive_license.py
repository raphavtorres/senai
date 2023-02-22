from datetime import date

day_current = date.today().day
month_current = date.today().month
year_current = date.today().year

day_birth = int(input("Day you were born: "))
month_birth = int(input("Month you were born: "))
year_birth = int(input("Year you were born: "))

isValid = True

if year_current - year_birth > 18:
    pass
elif month_current < month_birth:
    isValid = False
elif month_current == month_birth and day_current < day_birth:
    isValid = False
else:
    pass

if isValid:
    print("You can get a driver's license!")
else:
    print("You can't get a driver's license!")
    
