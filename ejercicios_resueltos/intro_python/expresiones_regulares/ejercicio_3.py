# Creá un programa que verifique las siguientes condiciones:

# si un string dado tiene una h seguida de ninguna o más e.

# si un string dado tiene una h seguida de una o más e.

# si un string dado tiene una h seguida de dos o tres e.

def verificar(string):
    import re
    h1 = re.search(r'he*', string)
    h2 = re.search(r'he+', string)
    h3 = re.search(r'he{2,3}', string)
    print(h1, h2, h3)

verificar("hlado")