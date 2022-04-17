# Escribí un programa que obtenga, a partir de una lista de strings una lista con la longitud de esas strings e imprima la longitud de la lista de strings y los elementos de la lista de longitudes

def listar(lista_strings):
    longitud_lista = len(lista_strings)
    longitud_strings = []
    for list in lista_strings:
        longitud_strings.append(len(list))
    return print(longitud_lista, longitud_strings, lista_strings)

listar(["nico", "nic", "nicolas"])