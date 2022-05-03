# Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: _"Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"_)

def entre_guiones(string):
    import re
    extraer = re.findall(r'-(\w+)-?', string)
    print(extraer)

entre_guiones("nicolas-katz-2001_1020-fjd2_dd")