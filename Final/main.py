# El formato estándar (IEEE 802) para imprimir direcciones MAC-48 en forma amigable para los humanos es de seis grupos de dos dígitos hexadecimales, 
# separados por guiones - o dos puntos :

# ENUNCIADO
# Seguimiento algún usuario, en un día establecido, para ver el desplazamiento del usuario en
# el edificio donde se encuentra la red, a través de la MAC AP

import re
import os
import subprocess

try:
    import pandas as pd
except:
    subprocess.call('pip3 install pandas', shell=True)
    import pandas as pd

with open("trafico.txt", "r") as file:
    #Separa todo en listas
    datos = file.read().replace("\n", ";").split(";")

    expresionMAC = '^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    expresionMACAP = '^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}):UM$'

    #Borra los titulos
    for i in range(0, 9):
        datos.pop(0)


    datosOrg = []
    listUsuario = []
    listMACAP = []
    listMACCliente = []
    cont = 0

    #Hace una lista de un registro y lo guarda dentro de otra (lista de listas)
    for i in datos:
        listUsuario.append(i)
        cont += 1
        if cont == 9:
            datosOrg.append(listUsuario)
            listUsuario = []
            cont = 0

    for i in datosOrg:
        #Guardo usuarios
        if not i[1] in listUsuario and i[1] != "":
            listUsuario.append(i[1])

        #Guardo MAC Clientes
        if not i[8] in listMACCliente and re.match(expresionMAC, i[8]):
            listMACCliente.append(i[8])

        #Guardo MAC AP's
        if not i[7] in listMACAP and re.match(expresionMACAP, i[7]):
            listMACAP.append(i[7])

    usuarioSelec = ""
    
    print("Selecione usuario:")
    for i in range(0, len(listUsuario)):
        print(str(i) + "- " + str(listUsuario[i]))
    usuarioSelec = input("Numero del usuario o una letra para salir >>")

    while(usuarioSelec.isdigit()):
        
        usuarioSelec = int(usuarioSelec)

        print("\nUsuario seleccionado:", listUsuario[usuarioSelec])

        #Guardo registros del usuario seleccionado
        listFecha = []
        for i in datosOrg:
            if listUsuario[usuarioSelec] in i and not i[2] in listFecha:
                listFecha.append(i[2])


        #No muestra las fechas repetidas
        print("Selecione fecha:")
        for i in range(0, len(listFecha)):
            if(listFecha[i][:10] != listFecha[i-1][:10] and i != 0):
                print(str(i) + "- " + str(listFecha[i][:10]))
            elif i == 0:
                print(str(i) + "- " + str(listFecha[i][:10]))

        fechaSelec = int(input("Numero de la fecha >>"))

        file = open("trafico_" + listUsuario[usuarioSelec] + "_" + listFecha[fechaSelec][:10].replace("/", "-") + ".csv", "w")
        file.write("Usuario;MAC Cliente;MAC AP;Inicio de conexión;Fin de conexión\n")

        for i in datosOrg:
            if listUsuario[usuarioSelec] in i and listFecha[fechaSelec][:10] == i[2][:10]:
                file.write(i[1] + ";" + i[8] + ";" + i[7] + ";" + i[2] + ";" + i[3] + "\n")
        file.close()

        csv = pd.read_csv("trafico_" + listUsuario[usuarioSelec] + "_" + listFecha[fechaSelec][:10].replace("/", "-") + ".csv", sep=';')
        print("\n", csv)

        input("\nArchivo generado, presiona Enter para continuar")

        print("\nSelecione usuario:")
        for i in range(0, len(listUsuario)):
            print(str(i) + "- " + str(listUsuario[i]))

        usuarioSelec = input("Numero del usuario o una letra para salir >>")
