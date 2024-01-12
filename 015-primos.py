# Programa para detectar si un número es primo.

# -------------- IMPORTACIÓN DE MÓDULOS -------------

#---------------- DECLARAR VARIABLES ---------------
salirPrograma = False
numero = ''

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
        print('Si desea intentar con otro número oprima "s", de lo contrario oprima "n" para salir.')
        eleccion = input()
        if eleccion == 'N' or eleccion == 'n':
            opcionElegida = True
        elif eleccion == 's' or eleccion == 'S':
            opcionElegida = False
        else:
            print(f'La tecla oprimida -{eleccion}- no es una opción elegible. La respuesta por defecto "Salir" se aplicará.')
            opcionElegida = True
    return opcionElegida

# Funcion 3 - Esvaluar si es numero primo
def esPrimo(num):
    if num == 1 or num == 2:
        return True
    elif num == 0:
        return False
    else:
        contador = 0
        for x in range(2,num-1):
            if num % x == 0:
                contador += 1
        if contador >= 1:
            return False
        else:
            return True

# ------------ EJECUCIÓN PRINCIPAL ----------------
while salirPrograma == False:
    # Obtener el número
    numero = input("Ingresa un numero cualquiera - Nota: El número será convertido a entero.\n")
    esNumero = verificarTipoDato(numero, int)
    if esNumero == True:
        numero = abs(int(numero))
        resultado = esPrimo(numero)
        if resultado == True:
            print(f"El número {numero} si es primo.")
        else:
            print(f"El número {numero} no es primo.")
    else:
        print(f"Lo siento ingresaste un dato que no se puede calcular ({numero}), intentalo de nuevo.")
    salirPrograma = continuarSiNo()