# Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.

def esMultiplo(entero1, entero2):
    if(entero1 % entero2 == 0):
        return print("El primer entero es multiplo del otro")
    if(entero2 % entero1 == 0):
        return print("El segundo entero es multiplo del otro")
    return print("Ninguno es multiplo del otro")

def enteros(entero1, entero2):
    esMultiplo(entero1, entero2)

enteros(4, 6)
enteros(6, 3)
enteros(13, 11)