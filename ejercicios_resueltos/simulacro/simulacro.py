# RE

import re

def cuantas_veces(string):
    resultado = re.findall("bc9", string)
    return len(resultado)

def sin_c(string):
    return re.findall("aa([^c]*?)gg", string)

print(cuantas_veces("xsabc9cabcb3sabc9"))
print(sin_c("ttaatatggttaacatgg"))

# MdA

import os, glob

def unir_txt():
    os.mkdir("Resultado")
    lista_txt = glob.glob("*.txt")
    salida = open("Resultado\\texto_completo,txt", "a")
    for txt in lista_txt:
        archivo = open(txt, "r")
        salida.write(archivo.read())
        archivo.close()
    salida.close()

unir_txt()

# POO

class Auto():
    def __init__(self):
        self.consumo = 0.05
        self.rpm = 0
        self.cambio = None
    
    def arrancar(self):
        self.cambio = 1
        self.rpm = 500

    def subirCambio(self):
        if self.cambio < 5:
            self.cambio += 1
        
    def bajarCambio(self):
        if self.cambio > 1:
            self.cambio -= 1
    
    def subirRPM(self, cantidad):
        if self.rpm - cantidad >= 0:
            self.rpm -= cantidad
        else:
            self.rpm = 0
    
    def velocidad(self):
        return ((self.rpm / 100) * 0.5 + (self.cambio / 2))

    def consumoActualPorKm(self):
        if self.rpm > 3000:
            if self.cambio == 1:
                return (self.consumo * ((self.rpm - 2500) / 500) * 3)
            elif self.cambio == 2:
                return (self.consumo * ((self.rpm - 2500) / 500) * 2)
            elif self.cambio >= 5:
                return (self.consumo * ((self.rpm - 2500) / 500))
        elif self.cambio == 1:
            return (self.consumo * 3)
        elif self.cambio == 2:
            return (self.cambio * 2)
        else:
            return (self.consumo)
    
    def cambioActual(self):
        return (self.cambio)
    
    def rpmActual(self):
        return (self.rpm)

auto = Auto()

# MdE

# ZeroDivisionError

def obtener_media(lista):
    sumatoria = 0
    try:
        for valor in lista:
            if valor < 0:
                raise ValueError("no negativos")
            sumatoria += valor
            longitud = len(lista)
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    except TypeError:
        print("solo numeros")
    except ValueError as err:
        print(err)
    except:
        print("general")
    else: 
        return print(sumatoria / longitud)
    finally:
        print("termine la funcion")
## TypeError

obtener_media([-1, 2, 3, 4])