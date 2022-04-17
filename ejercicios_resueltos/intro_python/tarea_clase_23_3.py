def datos_personales(folder, mode, object):
    import os
    os.mkdir(folder)
    path = os.getcwd() + "\\" + folder + "\\datos.txt"
    with open(path, mode) as my_dates:
        my_dates.write(object)

datos_personales("datos_personales", "w", "nicolas katz 20 años")