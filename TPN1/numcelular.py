import re

regex = re.compile(r'^\+(?:(?:00)549)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$')

numero = input("Ingrese el numero celular: ")

if(regex.search(numero)):
    print("Numero correcto")
else:
    print("Numero incorrecto")
