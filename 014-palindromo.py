# Programa para detectar si una palabra es un palindromo o no.

# -------------- IMPORTACIÓN DE MÓDULOS -------------

#---------------- DECLARAR VARIABLES ---------------
salirPrograma = False
palabraOriginal = ''

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
        print('Si desea intentar con otra cadena oprima "s", de lo contrario oprima "n" para salir.')
        eleccion = input()
        if eleccion == 'N' or eleccion == 'n':
            opcionElegida = True
        elif eleccion == 's' or eleccion == 'S':
            opcionElegida = False
        else:
            print(f'La tecla oprimida -{eleccion}- no es una opción elegible. La respuesta por defecto "Salir" se aplicará.')
            opcionElegida = True
    return opcionElegida

# Funcion #3 - Comparacion de cadenas
def comparasionCadenas(cadena1, cadena2):
    if cadena1 == cadena2:
        return True
    else:
        return False

# ------------ EJECUCIÓN PRINCIPAL ----------------
while salirPrograma == False:
    print("Vamos a ver cuanto sabes de palíndromos, escribe uno:")
    palabraOriginal = input()
    esCadena = verificarTipoDato(palabraOriginal, str)
    if esCadena == True:
        palabra = palabraOriginal.lower()
        palabra = palabra.replace(' ', '')
        palabraReves = palabra[::-1]
        resultado = comparasionCadenas(palabra, palabraReves)
    else:
        print(f"La cadena ingresada ({palabraOriginal}) no es una cadena válida. Prueba de nuevo.")
    # Mostrar resultado:
    if resultado == True:
        print(f"La cadena {palabraOriginal} es un palíndromo.")
    else:
        print(f"La cadena {palabraOriginal} no es un palíndromo.")
    salirPrograma = continuarSiNo()