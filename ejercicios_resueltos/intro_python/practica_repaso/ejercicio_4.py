# Realizá un programa que a partir de una lista mixta (que contiene distintos tipos de datos) imprima cuántos enteros tiene y además en el caso de los elementos que sean strings hay que crear una nueva lista con estos strings pero reemplazando al A por la U (tanto mayúscula como minúscula) y luego imprimir estos elementos.

string = []
intriger = []
boolean = []

def lista_mixta(lista):
    for dato in lista:
        if(type(dato) is str):
            nuevo__dato = dato.replace("a", "u")
            string.append(nuevo__dato)
        elif(type(dato) == int):
            intriger.append(dato)
        else:
            boolean.append(dato)
    return print(string, intriger, boolean)

lista_mixta(["nicolas", 20, True, "hola", False, "nico", 1, 40, "gol", True])