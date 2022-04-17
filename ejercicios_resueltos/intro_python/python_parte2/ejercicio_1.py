# Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.

def firstLetter(string):
    try:
        letter = string[0]
        if(letter == letter.upper()):
            return print("La primera letra de mi string es una mayuscula")
        elif(letter == letter.lower()):
            return print("La primera letra de mi string es una minuscula")  
    except:
        return print("Debes introducir un dato de tipo string")

firstLetter("Nicolas")
firstLetter("nicolas")
firstLetter(1)

