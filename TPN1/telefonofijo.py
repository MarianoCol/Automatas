import re

numero = input("Ingresar numero de telefono: ")
m = re.match('\+[1-9]{1}[0-9]{3,14}$',numero)

if m:
    print("Es un numero valido")
else:
    print("No es un numero valido")