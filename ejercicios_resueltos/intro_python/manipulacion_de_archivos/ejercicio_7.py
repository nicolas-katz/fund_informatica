# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

# def palabra_mas_larga():
#     import os
#     archivo = open(os.getcwd() + "\\ejercicio_1.txt", "r")
#     texto = archivo.read()
#     cada_palabra = texto.split()
#     mas_larga = max(cada_palabra, key=len)
#     print(mas_larga, len(mas_larga))
    
# palabra_mas_larga()

def mas_larga():
    caracteres = 0
    palabra_ = ''
    with open("ejercicio_1.txt", "r") as archivo:
        for palabra in archivo.read().split():
            if(len(palabra) > caracteres):
                caracteres = len(palabra)
                palabra_ = palabra
        return print(palabra_, caracteres)

mas_larga()