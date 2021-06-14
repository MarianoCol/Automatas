import re

email = input("Ingresar email: ")
m = re.match('[^@]+@[^@]+\.[^@]+',email)

if m:
    print("Es una direccion email")
else:
    print("No es una direccion email")