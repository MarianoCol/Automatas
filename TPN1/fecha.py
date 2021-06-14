import re

fecha = input("Ingresar una fecha: ")
tipo1 = re.match('(\d+/\d+/\d+)',fecha)
tipo2 = re.match('(\d+-\d+-\d+)',fecha)

if tipo1 or tipo2:
    print("Es una fecha correcta")
else:
    print("Es una fecha incorrecta")