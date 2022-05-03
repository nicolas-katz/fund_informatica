# Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

def palabra_unida(string):
    import re
    palabra = re.findall(r"(\w[^\d]+)_(\w[^\d]+)", string)
    print(palabra)

palabra_unida("nico_jdjdj1_jdsjd")