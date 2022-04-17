# Escribí un programa que lea un archivo e imprima las primeras n líneas.

def imprimir_lineas(archivo, modo, num_lineas):
    import os
    path = os.getcwd() + archivo
    with open(path, modo) as arch:
        lista = arch.readlines(num_lineas)
        return print(lista)


imprimir_lineas("\ejercicio_1.txt", "r", 10)

## Esta mal hecho. Consultar en clase