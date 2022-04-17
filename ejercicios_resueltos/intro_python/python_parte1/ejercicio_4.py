# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas

def persona(nombre, apellido1, apellido2):
    return print(nombre[0].upper(), apellido1[0].upper(), apellido2[0].upper())

persona("nicolas", "katz", "silberman")