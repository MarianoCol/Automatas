import re
regex = re.compile(r'^/(ftp|http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/')
URL = input("Ingrese URL: ")

if (regex.match(URL)):
    print("URL Correcta")
else:
    print("URL Incorrecta")