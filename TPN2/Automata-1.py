import re
 
def caracter(character):
    global simbolo
    simbolo=""
    global Fin
    Fin=""
    caracterA="a"
    caracterB="b"
     
    if(re.match(caracterB,character)):
        simbolo=" caracter "
        return 0
    else:
        if(re.match(caracterA,character)):
            simbolo="Operador"
            return 1
        else:
            if(character==Fin):
                return 2
         
        print("Error el ",character,"no es valido")
        exit()
 
def encabezado():
    print("""|  Edo. Actual |Caracter |  Simbolo  |Edo. Siguiente |""")
    body()
 
def contenido(estadosig,character,simbolo,estado):
    print("|     ",estadosig,"      |  ",character,"    |",simbolo," |     ",estado,"       |")
    body()
 
def body():
    print("+--------------+---------+-----------+---------------+")
 

tabla=[[1,1,"E"],[1,2,"E"],[1,3,"E"],[1, 3,"A"]]
estado = 0
 
print ("""+-------------------------------------+
|    Ingrese una cadena a evaluar:    |
+-------------------------------------+""")
cadena = input()

if cadena == "ba" or cadena == "a" or cadena == "aa":
    body()
    print("""|                Cadena Valida :)                    |
+----------------------------------------------------+""")
else:
    body()
    encabezado()  
    for  character in cadena:
        estadosig=estado
        
        charcaracter= caracter(character)

        estado=tabla[estado][charcaracter]

        if (estado=="E"):
            print("|     ",estadosig,"      |  ",character,"    |",simbolo," |     ",estado,"       |")
            body()
            print("""|              Cadena No Valida :(                   |
    +----------------------------------------------------+""")
            exit()
        contenido(estadosig,character,simbolo,estado)
        
    if(estado!=3):
            print("""|              Cadena No Valida :(                   |
    +----------------------------------------------------+""")
    
    if(estado==3):
        print("|     ",estado,"      |         |    FND    |               |")
        body()
        print("""|                Cadena Valida :)                    |
+----------------------------------------------------+""")
