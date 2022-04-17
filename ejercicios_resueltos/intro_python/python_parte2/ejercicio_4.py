# Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:

# Zona	Ubicación	        Costo/gramo
# 1	    América del Sur	    10.00 dólares
# 2	    América Central	    15.00 dólares
# 3	    América del Norte   18.00 dólares
# 4	    Europa	            24.00 dólares
# 5	    Asia	            30.00 dólares

# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

def transporte_internacional(ubicacion, costo_por_gramo, kilo):
    if(kilo < 5 and kilo > 0):
        if(ubicacion == "América del Sur"):
            return print("El costo de servicio sale " + costo_por_gramo)
        elif(ubicacion == "América Central"):
            return print("El costo de servicio sale " + costo_por_gramo)
        elif(ubicacion == "América del Norte"):
            return print("El costo de servicio sale " + costo_por_gramo)
        elif(ubicacion == "Europa"):
            return print("El costo de servicio sale " + costo_por_gramo)
        elif(ubicacion == "Asia"):
            return print("El costo de servicio sale " + costo_por_gramo)
        else:
            return print("No trabajamos en ese continente. Intenta introducir un continente valido que son los siguientes: América del Sur, América Central, América del Norte, Europa o Asia")
    else:
        return print("No realizamos pedidos mayores o iguales a 5kg.")

transporte_internacional("América del Sur", "10.00 dolares", 1)
transporte_internacional("América Central", "15.00 dolares", 2)
transporte_internacional("América del Norte", "18.00 dolares", 3)
transporte_internacional("Europa", "24.00 dolares", 4)
transporte_internacional("Asia", "30.00 dolares", 2)
transporte_internacional("América del Sur", "10.00 dolares", 6)
transporte_internacional("América del Sur", "10.00 dolares", 0)
