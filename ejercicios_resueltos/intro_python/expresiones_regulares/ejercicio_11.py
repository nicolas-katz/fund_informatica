# Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: _["Práctica Python", "Práctica C++", "Práctica Fortran"]_).

def empiezan_con_p(lista):
    import re
    sum_palabras = 0
    for palabra in lista:
        encontro = re.findall(r'^p', palabra, flags=re.I)
        if encontro:
            sum_palabras += 1
    return print(sum_palabras)

empiezan_con_p(["Práctica Python", "Práctica C++", "Práctica Fortran"])