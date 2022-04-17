# ##### **Ejercicio 15**
# Creá un programa para gestionar datos de los socios de un club, el cual permita:

# * Cargar la información de los socios en un diccionario para acceder por número de socio. Los datos que se deben almacenar son: _número_, _nombre y apellido_, _fecha de ingreso (ddmmaaaa)_, _cuota al dia (s/n)_ (el programa tiene que dejar de cargar cuando se ingrese el _número_ **0**). El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

#   **Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día**
  
#   **Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día**
  
#   **Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día**

# * Informar la cantidad de socios que tiene el club.

# * Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

# * Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

# * Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

# * Imprimir el listado de socios completos.

# Definir las funciones que creas necesarias.

socios = [
    {"number": 1, "name": "Florencia Ocampo", "entry": "14/09/2001", "payment": "No tiene las coutas al día"},
    {"number": 2, "name": "David Estévez", "entry": "14/09/2001", "payment": "No tiene las coutas al día"},
    {"number": 3, "name": "Sofía Cáceres", "entry": "14/09/2001", "payment": "No tiene las coutas al día"}    
]

def count_members(members):
    return print(len(members))

count_members(socios)

def payment(id_user, members):
    for member in members:
        if(member["number"] == id_user):
            member["payment"] = "Si tiene las cuotas al día"
            return print(member["payment"])

payment(1, socios)

def changingEntries(newDate, members):
    for member in members:
        if(member["entry"] == "14/09/2001"):
            member["entry"] = newDate
    return print(members)

changingEntries("22/10/2017", socios)

def deleteMember(name, members, id):
    for member in members:
        if(member["name"] == name):
            members.pop(id - 1)
    return print(members)

deleteMember("Florencia Ocampo", socios, 1)

def printAll(members):
    return print(members)

printAll(socios)