# Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

def verificar_string(string):
    import re
    todos = re.findall(r".", string)
    permitido = re.findall(r"\w", string)
    print(todos == permitido)

verificar_string("nico")
