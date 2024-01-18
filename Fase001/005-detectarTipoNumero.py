# Programa para detectar si el número ingresado es par, impar, negativo, positivo y/o neutro.

# -------------- DECLARACIÓN VARIABLES ----------------
numeroEvaluado = ''
salirPrograma = False

# ----------------DEFINIR FUNCIONES -----------------
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

# Función 2 - Verificar si es par o impar
def esParImpar(numero):
    if (numero % 2 == 0):
        parImpar = 'par'
    else:
        parImpar = 'impar'
    return parImpar

# Funcion 3 - Verificar si es positivo o negativo
def esPositivoNegativo(numero):
    if numero < 0:
        signoNumero = 'negativo'
    elif numero > 0:
        signoNumero = 'positivo'
    return signoNumero

# Funcion 4 - Evaluadora de continuidad
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

# ------------------ EJECUCIÓN PRINCIPAL ----------------------
while salirPrograma == False:
    print('Escriba un número entero: ')
    # Ingreso de datos por tecclado
    numeroEvaluado = input('Dato:')
    # Evaluar si el dato es un número entero
    esEvaluable = verificarTipoDato(numeroEvaluado, int)
    if esEvaluable == True:
        numeroEvaluado = int(numeroEvaluado)
        # Evaluar si es cero.
        if numeroEvaluado == 0:
            print(f'El número {numeroEvaluado} es par y es neutro.')
        # Llamar funciones evaluadoras.
        else:
            claseNumero = esParImpar(numeroEvaluado)
            signoNumero = esPositivoNegativo(numeroEvaluado)
    else:
        print(f'{numeroEvaluado} no es un número entero')
    # Imprimir resultado en pantalla.
    print(f'El número {numeroEvaluado} es {claseNumero} y es {signoNumero}.')
    # Ofrecer opciones de ciclo
    salirPrograma = continuarSiNo()