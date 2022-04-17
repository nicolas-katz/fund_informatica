# Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado. Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.

def dados(number):
    try:
        if(number > 6 or number < 1):
            return print("Debes introducir un numero menor o igual a 6 y mayor o igual a 1")
        else:
            if(number == 1): 
                return print("2")
            elif(number == 2): 
                return print("3")
            elif(number == 3): 
                return print("4")
            elif(number == 4): 
                return print("5")
            elif(number == 5): 
                return print("6")
            elif(number == 6): 
                return print("1")
    except:
        return print("Debes introducir un numero")

dados(1)
dados(2)
dados(3)
dados(4)
dados(5)
dados(6)
dados("1")