# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def imprimir_cant_lineas():
    import os
    archivo = open(os.getcwd() + "\\ejercicio_1.txt", "r")
    palabras = archivo.read()
    cant = palabras.split()
    print(cant)

    archivo.close()

imprimir_cant_lineas()