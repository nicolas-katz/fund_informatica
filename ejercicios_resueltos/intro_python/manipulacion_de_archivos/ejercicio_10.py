# Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.

import glob

def unir_txt():
    lista_txt = glob.glob("*.txt")
    nuevo_archivo = open("texto_completo.txt", "w")
    for txt in lista_txt:
        archivo = open(txt, "r")
        nuevo_archivo.write(archivo.read())
        archivo.close()
    nuevo_archivo.close()

unir_txt()