# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

import re
import os

# def frecuencia():
#     contador = {}
#     total = len(open(os.getcwd() + "\\ejercicio_1.txt", "r").read().split())

#     patron = re.compile(r"(\w+)")
#     with open(os.getcwd() + "\\ejercicio_1.txt", "r") as texto:
#         for linea in texto.readlines():
#             m = patron.findall(linea)
#             for palabra in m:
#                 palabra = palabra.lower()
#                 if palabra in contador:
#                     contador[palabra] = (contador[palabra] + 1) / total
#                 else:
#                     contador[palabra] = 1 / total
#     print(contador)

# frecuencia()

def _frecuencia():
    frecuencia = {}
    with open("ejercicio_1.txt", "r") as texto:
        palabras = texto.read().split()
        for palabra in palabras:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
        for palabra in frecuencia.keys():
            frecuencia[palabra] = round(frecuencia[palabra] / len(palabras), 3)
    return print(frecuencia)

_frecuencia()