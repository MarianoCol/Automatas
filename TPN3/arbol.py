# Analizador sintactico predictivo para operaciones aritméticas + - y ()
# Ejemplo de entrada id+id-id
# Gramatica
# E → T E'
# E' → + T E'| ε
# T → F T'
# T' → - F T'| ε
# F → ( E ) | i


def obtener_col(simbolo_entrada):  # obtiene columna tabla de analisis
    if(simbolo_entrada.isdigit()):
        return 0
    else:
        if(simbolo_entrada == '+'):
            return 1
        else:
            if(simbolo_entrada == '-'):
                return 2
            else:
                if(simbolo_entrada == '('):
                    return 3
                else:
                    if(simbolo_entrada == ')'):
                        return 4
                    else:
                        if(simbolo_entrada == '$'):
                            return 5
                        else:
                            raise Exception(
                                "Simbolo no aceptado por el analizador sintactico")


def obtener_fila(no_terminal):  # obtiene fila tabla de analisis
    if(no_terminal == 'E'):
        return 0
    else:
        if(no_terminal == 'E\''):
            return 1
        else:
            if(no_terminal == 'T'):
                return 2
            else:
                if(no_terminal == 'T\''):
                    return 3
                else:
                    if(no_terminal == 'F'):
                        return 4
                    else:
                        raise Exception(
                            "Simbolo no aceptado por el analizador sintactico")

# Definicion funciones de la pila


class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def insertar(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[len(self.items)-1]

    def tamano(self):
        return len(self.items)

    def contenido(self):
        return (self.items)


# Definicion de la tabla
tabla = [["E->TE'", "", "", "E->TE'", "", ""], ["", "E'->+TE'", "", "", "E'->e", "E'->e"], ["T->FT'", "",
                                                                                            "", "T->FT'", "", ""], ["", "T'->e", "T'->-FT'", "", "T'->e", "T'->e"], ["F->2", "", "", "F->(E)", "", ""]]
p = Pila()
p.insertar('$')
p.insertar('E')
entrada = list(input("Ingrese la funcion y un simbolo $ al final: "))
"""
bucle = True
entrada = []
while bucle is True:
    valor = input("Ingrese los numeros y simbolos a sumar - Ingrese $ para finalizar: ")
    entrada.append(valor)
    if valor == '$':
        bucle = False
"""
simbolo_entrada = entrada[0]
if simbolo_entrada.isdigit() == False:
    raise Exception("Cadena no valida")
entrada_2 = entrada[:]
salida = ''


# Inicio arbol sintactico
print('\nArbol de sintáctico')
print('\nPILA \t\t\t\t ENTRADA \t\t\t\t SALIDA')
print(str(p.contenido()) + '\t\t\t' + str(entrada_2) + '\t\t\t' + str(salida))
for simbolo_entrada in entrada:
    cima_pila = p.inspeccionar()
    while(cima_pila != simbolo_entrada):
        try:
            col = obtener_col(simbolo_entrada)
            fil = obtener_fila(cima_pila)
            if(col == 0 and fil == 4):
                tabla[fil][col] = 'F->'+simbolo_entrada
            salida = tabla[fil][col]
            if(salida != ''):
                print(p.inspeccionar())
                p.extraer()
                posicion = salida.find('>')
                produccion = salida[posicion+1:len(salida)]
                produccion_pila = []
                for simbolo in produccion:
                    if(simbolo != '\''):
                        posicion_2 = produccion.find(simbolo)
                        if(produccion[posicion_2+1:posicion_2+2] == '\''):
                            produccion_pila.append(simbolo + '\'')
                        else:
                            produccion_pila.append(simbolo)
                for simbolo in reversed(produccion_pila):
                    if(simbolo != 'e'):
                        p.insertar(simbolo)
            print(str(p.contenido()) + '\t\t\t' +
                  str(entrada_2) + '\t\t\t' + str(salida))
            cima_pila = p.inspeccionar()
        except ValueError:
            print("Cadena no valida")
    if(simbolo_entrada == '$' and p.inspeccionar() == '$'):
        print("\nArbol sintáctico construido!")
    else:
        print("\nValor seleccionado: "+p.inspeccionar())
        p.extraer()
        entrada_2.pop(0)
        print(str(p.contenido()) + '\t\t\t' + str(entrada_2) + '\t\t\t')

# Calculadora
valAnt = ''
for pos, val in enumerate(entrada):
    if pos == 0:
        resultado = int(entrada[0])
    if(val.isdigit()):
        if(pos != 0 and valAnt == '+'):
            resultado += int(val)
        if(pos != 0 and valAnt == '-'):
            resultado -= int(val)
    if(val != '(' and val != ')'):
        valAnt = val

print("\nEl resultado de la funcion es: "+str(resultado))
