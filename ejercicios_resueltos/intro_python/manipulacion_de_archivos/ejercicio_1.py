# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

def no_empiezan_con_string(string):
    import os
    archivo = open(os.getcwd() + "\\ejercicio_1.txt", "r")
    lineas = archivo.readlines()
    sum = 0
    for linea in lineas:
        if not linea.startswith(string):
            sum += 1
    archivo.close()
    return print(sum)

no_empiezan_con_string("p")