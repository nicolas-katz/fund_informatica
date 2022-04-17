# Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.

def horas_y_minutos(minutos):
    if(minutos < 60):
        return print(str(minutos) + " minutos")
    else:
        min = int(minutos % 60)
        horas = int((minutos - min) / 60)
        string_minutos = str(min)
        string_horas = str(horas)
        return print(string_horas + " horas y " + string_minutos + " minutos")

horas_y_minutos(135)
horas_y_minutos(30)