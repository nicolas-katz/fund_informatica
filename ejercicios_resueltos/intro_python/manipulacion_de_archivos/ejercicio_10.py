# Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.

import os, glob

def unir_txt():
    lista_txt = glob.glob("*.txt")
    salida = open(os.getcwd() + "\\texto_completo.txt", "a")
    for txt in lista_txt:
        archivo = open(txt, "r")
        salida.write(archivo.read())
        archivo.close()
    salida.close()

unir_txt()