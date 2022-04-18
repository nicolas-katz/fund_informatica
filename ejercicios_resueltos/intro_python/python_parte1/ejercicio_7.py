# Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.

def sueldo_comerciante(sueldo_base, num_de_ventas):
    comision_por_venta = num_de_ventas * (sueldo_base * 0.10)
    salario_total = sueldo_base + comision_por_venta
    return print(salario_total, comision_por_venta)

sueldo_comerciante(10000, 4)