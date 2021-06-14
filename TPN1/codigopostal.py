import re

codigo = input("Ingresar codigo postal: ")
m = re.match('^[A-Z]{1}[0-9]{4}[A-Z]{3}',codigo)

if m:
    print("Es una codigo postal")
else:
    print("No es un codigo postal")