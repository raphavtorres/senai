# FALSY: (the oposite is truthy)
list = []
dictionary = {}
set = set()
string = ''
integer = 0
float = 0.0
nothing = None
boolean = False
interval = range(00)


def falsy(value):
    return 'falsy' if not value else 'truthy'






# dir, hasattr e getattr

# dir ==> shows all the names inside "string"
string = "raphael"
# Debug console
print(string)

# hasattr ==> checks if a specific object has a specific name inside "string"
if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

# getattr ==> get a method in a dinamic way, python understands that you're talking about a method
method = 'lower'
if hasattr(string, method):
    print(f'Existe {method}')
    print(getattr(string, method)())
else:
    print(f"Method {method} doesn't exists")
