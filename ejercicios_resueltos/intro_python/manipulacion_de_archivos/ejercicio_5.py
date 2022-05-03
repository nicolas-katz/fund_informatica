# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

def reemplazar_letra(string):
    archivo = open("ejercicio_1.txt", "r")
    palabras = archivo.read()
    texto_nuevo = palabras.replace(string, string + "\n")
    archivo.close()
    nuevo_archivo = open("ejercicio_5.txt", "w")
    nuevo_archivo.write(texto_nuevo)
    nuevo_archivo.close()


reemplazar_letra("a")