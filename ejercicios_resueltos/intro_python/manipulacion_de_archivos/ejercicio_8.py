# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def guardar_en_uno():
    arch1 = open("ejercicio_1.txt", "r")
    arch1_texto = arch1.read()
    arch1.close()
    arch2 = open("ejercicio_5.txt", "r")
    arch2_texto = arch2.read()
    arch2.close()
    arch3 = open("ejercicio_6.txt", "a")
    arch3.writelines([arch1_texto, arch2_texto])
    arch3.close()

guardar_en_uno()
