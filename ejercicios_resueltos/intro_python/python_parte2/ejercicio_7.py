# Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.

lista = []
i = 14

while i > 0:
    lista.append(i)
    i -= 1
    if i == 0:
        print(lista)
        break
