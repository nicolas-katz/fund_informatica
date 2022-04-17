# Realizá un programa que declare tres listas _lista1_, _lista2_ y _lista3_, donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la _lista3_ la suma de los elementos de la _lista1_ y la _lista2_ (es decir, el primer elemento de la _lista3_ tiene que ser la suma del primer elemento de la _lista1_ y el primero de la _lista2_)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = []

def lists(list_one, list_two, list_three):
    for list in range(0, 4):
        list_three.append(list_one[list] + list_two[list])
    return print(list_three)

lists(list1, list2 ,list3)