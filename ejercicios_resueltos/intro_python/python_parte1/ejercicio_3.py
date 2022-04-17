# Escribir un programa que pregunte el nombre y apellido al usuario y lo salude.

from re import S


def saludar(nombre, apellido):
    return print("¡Hola " + nombre + " " + apellido + ", espero que estes bien!")

saludar("Nicolas", "Katz")