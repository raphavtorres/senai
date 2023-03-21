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
