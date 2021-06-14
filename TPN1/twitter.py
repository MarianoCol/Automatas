import re

usuario = input("Ingresar usuario de Twitter: ")
m = re.match('^@(\w){1,15}$',usuario)

if m:
    print("Es un usuario valido")
else:
    print("No es un usuario valido")
