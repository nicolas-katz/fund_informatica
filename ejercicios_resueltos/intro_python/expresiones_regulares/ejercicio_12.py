# Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (**|**).

def reemplazar_por_barra(string):
    import re
    caracteres_especiales = re.findall('[\s\:_]', string)
    for c in caracteres_especiales:
        with open("re12.txt", "w") as ex:
            ex.write(c)
    with open("re12.txt", "r") as ex:
        ex.read().replace(c, "**|**")

reemplazar_por_barra("fjijcdsc_:::_ fr fr : _ dedwewf:")