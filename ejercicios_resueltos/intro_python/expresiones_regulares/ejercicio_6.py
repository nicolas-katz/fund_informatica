# Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

def lista_strings(lista, frase):
    import re
    estan = []
    no_estan = []
    verify = re.findall(r'[a-zA-Z]', frase, flags=re.I)
    for letra in lista:
        if letra in verify:
            estan.append(letra)
        else: 
            no_estan.append(letra)
    return print(estan, no_estan)

lista_strings(["a", "b", "c", "d", "e", "f", "g"], "nicolas")