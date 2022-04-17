# Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

def dia_de_semana(number):
    if(number >=1 and number <= 7):
        return print(number)
    else:
        return print("El numero esta fuera de rango. Vuelve a intentarlo.")

dia_de_semana(1)
dia_de_semana(3)
dia_de_semana(5)
dia_de_semana(0)
dia_de_semana(10)