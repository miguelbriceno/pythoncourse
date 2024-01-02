# Programa para sumar varios números hasta que se le indique lo contrario

#---------------- DECLARAR VARIABLES ---------------
salirPrograma = False
total = 0
# --------------- DEFINIR FUNCIONES -----------------
# Funcion 1 - Verificar el tipo de dato para continuar
def verificarTipoDato(datoIngresado, tipoBuscado):
    tipoDatoIngresado = False
    while tipoDatoIngresado == False:
        if type(datoIngresado) == tipoBuscado:
            tipoDatoIngresado = True
        else:
            try:
                tipoBuscado(datoIngresado)
                tipoDatoIngresado = True
            except:
                #print(f'Error000 - No se puede cambiar {datoIngresado} al tipo de dato {tipoBuscado}')
                break
    return tipoDatoIngresado

# Funcion 2 - Evaluadora de continuidad
def continuarSiNo():
    opcionElegida = ''
    while opcionElegida == '':
        print('Si desea añadir otro número oprima "s", de lo contrario oprima "n" para salir.')
        eleccion = input()
        if eleccion == 'N' or eleccion == 'n':
            opcionElegida = True
        elif eleccion == 's' or eleccion == 'S':
            opcionElegida = False
        else:
            print(f'La tecla oprimida -{eleccion}- no es una opción elegible. La respuesta por defecto "Salir" se aplicará.')
            opcionElegida = True
    return opcionElegida

# Funcion 3 -  Añadir al acumulado.
def addAcumulado(numeroNuevo, acumulado):
    acumulado = acumulado + numeroNuevo
    return acumulado

# ------------ EJECUCIÓN PRINCIPAL ----------------
while salirPrograma == False:
    print('Bienvenido, vamos a sumar tanto números como desee.')
    print('Ingrese un número:')
    numero = input()
    esSumable = verificarTipoDato(numero, int)
    if esSumable == True:
        numero = int(numero)
        total = addAcumulado(numero, total)
        print(f'El total acumulado de la suma es de: {total}.')
    else:
        print(f'El dato ingresado: {numero} no es calculable en la operación.')
    salirPrograma = continuarSiNo()