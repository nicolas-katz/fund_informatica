# Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self, porcentaje):
        try:
            self.precio = self.precio - (self.precio * (porcentaje / 100))
            print(self.precio)
        except:
            print("Hubo un error. Asegurate de ingresar un valor numerico valido.")


mac = Notebook("apple", "2022", 200000)
lenovo = Notebook("lenovo", "2018", 120000)
hp = Notebook("hp", "2020", 180000)
mac.descuento(10)
lenovo.descuento(50)
hp.descuento(20)