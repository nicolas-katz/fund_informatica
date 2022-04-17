# Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.

# Recordá que la manera de copiar una lista en otra es:

# lista2 = list(lista1)

lista_1 = ["nicolas", "katz", "20 años", "1.60 de altura", "54 kg de peso"]
lista_2 = []

for item in reversed(lista_1):
    lista_2.append(item)

print(lista_2)