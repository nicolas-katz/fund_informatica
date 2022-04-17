# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

def cada_linea(archivo, modo, letra):
    import os
    path = os.getcwd() + archivo
    sum = 0
    with open(path, modo) as arch:
        lista = arch.readlines()
        for palabras in lista:
            if(palabras[0] != letra):
                sum += 1
        return print(sum)

cada_linea("\ejercicio_1.txt", "r", "a")