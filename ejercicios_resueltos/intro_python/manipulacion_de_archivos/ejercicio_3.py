# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def imprimir_lineas(n_lineas):
    archivo = open("ejercicio_1.txt", "r")
    lineas = archivo.readlines()
    cant_lineas = len(lineas) - n_lineas
    print(lineas[cant_lineas:])
    archivo.close()

imprimir_lineas(10)

