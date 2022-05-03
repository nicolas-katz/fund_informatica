# Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

def verificar_string(string):
    import re
    verify = re.search(r"\w", string)
    return print(verify or "No tiene ningun caracter permitido")

verificar_string("....")
verificar_string("nicolas")