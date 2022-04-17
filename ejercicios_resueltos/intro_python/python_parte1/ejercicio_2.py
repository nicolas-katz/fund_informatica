# Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayúscula (Asegurarse de que el string tenga la cantidad de caracteres suficientes).

def imprimir(string):
    if(len(string) < 7):
        return print("Debe introducir un string con más de 7 caracteres")
    else:
        return print(string[5].upper(), string[6].upper())

imprimir("nicolaskatz")