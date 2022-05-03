# Escribí un programa que lea un archivo e imprima las primeras n líneas.

def imprimir_lineas(n_lineas):
    archivo = open("ejercicio_1.txt", "r")
    lineas = archivo.readlines()
    for i in range(0, n_lineas):
        print(lineas[i])
    archivo.close()

imprimir_lineas(10)