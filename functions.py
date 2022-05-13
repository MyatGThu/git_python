def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('en'), 'George' )
print(greet('es'),'George' )
print(greet('fr'),'George' )

def addthree (b,c,d):
    add = b - c - d
    return add

x = addthree(8,9,10)
print(x)
