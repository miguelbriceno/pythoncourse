# Programa para multiplicar los valores de una tupla por números random

# Importacion de modulos
import random

#---------------- DECLARAR VARIABLES ---------------
salirPrograma = False

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
        print('Si desea realizar otra prueba oprima "s", de lo contrario oprima "n" para salir.')
        eleccion = input()
        if eleccion == 'N' or eleccion == 'n':
            opcionElegida = True
        elif eleccion == 's' or eleccion == 'S':
            opcionElegida = False
        else:
            print(f'La tecla oprimida -{eleccion}- no es una opción elegible. La respuesta por defecto "Salir" se aplicará.')
            opcionElegida = True
    return opcionElegida

# ------------ EJECUCIÓN PRINCIPAL ----------------
while salirPrograma == False:
    print('Vamos a empezar...\nEstas son las multiplicaciones:\n')
    # Creación litas y tupla
    pares = []
    impares = []
    numeros = (1,2,3,4,5,6,7,8,9)
    # Ciclo de multiplicaciones
    for x in numeros:
        multiplicador = random.randrange(100)
        dato = x * multiplicador
        print(f'{x} x {multiplicador} = {dato}')
        if dato % 2 == 0:
            pares.append(dato)
        else:
            impares.append(dato)
    # Imprimir listas al final
    print("")
    print('Resultados:')
    print('-' * 20)
    print('Pares:')
    print(f'{pares}')
    print('-' * 20)
    print('Impares:')
    print(f'{impares}')
    print('-' * 20)
    salirPrograma = continuarSiNo()