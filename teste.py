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

#-----------------------------------------------------------------------------------------------------  


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
    
    
#-----------------------------------------------------------------------------------------------------    
    
    
# Generator expression, Iterables and Iterators
# Iterator --> responsible for returning one element at a time
# It doesn't know much about the iterable
# "it only knows about the next element"

iterable = ["I", "Have", "__iter__"]
iterator = iterable.__iter__()  # tem __iter__ and __next__
# iterator = iter(iterable) (same as in the top)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# iterator runs out of values (ESGOTA os valores)

# Generators ==> functions that can pause
# All generators are iterators, but not the opposite
import sys
list = [n for n in range(1000)]  # in the memory since the moment I create it
generator = (n for n in range(1000))
print(sys.getsizeof(list))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

for n in generator:
    print(n)

#-----------------------------------------------------------------------------------------------------    
 
# Generator Function uses yield (pauses) instead of return


def generator(n=0):
    yield 1  # Pause
    print('continuing')  # raises an StopIneteration exception
    yield 2
    print('one more time')
    yield 3
    print("Vou terminar")
    return "Acabou"


gen = generator(n=0)
# print(gen.__iter__())
for n in gen:
    print(n)

       
#-----------------------------------------------------------------------------------------------------       
    
    
# FOR UNDER THE CARPET
name = "Raphael"
# for letter in name:
#     print(letter)

iterator = name.__iter__()
# iterator = iter(name)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
        
        
        
 #-----------------------------------------------------------------------------------------------------
# Generator Function uses yield (pauses) instead of return


def generator(n=0, max=10):
    while True:
        yield n
        n += 1
        if n > max:
            return


# gen is an generator object
gen = generator()
for i in gen:
    print(i)
