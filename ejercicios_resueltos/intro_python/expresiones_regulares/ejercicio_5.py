# Escribí un programa que diga si un string empieza con un número específico.

def numero(string, n):
    import re 
    empieza_con_num = re.search("^" + n, string)
    print(empieza_con_num)

numero("1nicolas", "1")