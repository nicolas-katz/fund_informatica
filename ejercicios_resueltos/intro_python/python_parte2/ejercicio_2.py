# Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).

def my_number_is(number):
    try:
        if(number >= 1):
            return print("Mi numero es positivo")
        elif(number == 0):
            return print("Mi numero es 0")
        else:
            return print("Mi numero es negativo")
    except:
       return print("Ocurrio un error. Asegurate de introducir un numero")

my_number_is(0)
my_number_is(10)
my_number_is(-3)
my_number_is("1")