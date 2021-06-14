import re

contraseña = input("Ingresar contraseña: ")
m = re.match('^(?=.*[a-z])(?=.*[A-Z])((?=.*\d)|(?=.*\W+)).{8,}',contraseña)

if m:
    print("Es una contraseña valida")
else:
    print("Es una contraseña invalida")

