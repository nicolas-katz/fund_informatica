# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

def eliminar_saltos():
    archivo = open("ejercicio_1.txt", "r")
    palabras = archivo.read()
    texto_nuevo = palabras.replace("\n", "")
    archivo.close()
    nuevo_archivo = open("ejercicio_6.txt", "w")
    nuevo_archivo.write(texto_nuevo)
    nuevo_archivo.close()


eliminar_saltos()