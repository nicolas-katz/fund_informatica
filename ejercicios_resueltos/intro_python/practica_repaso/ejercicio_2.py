# Realizá un programa que imprima la suma de todos los valores de un diccionario de números.

sum = 0

def sumatoria(sum, dic):
    for numero in dic:
        sum += numero
    return print(sum)

sumatoria(sum, {1, 2, 3, 4, 5})
sumatoria(sum, {5, 3, 31, 4})