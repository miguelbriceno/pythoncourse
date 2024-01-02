# Programa para devolver tres números ordenados de forma ascendente

#---------------- DECLARAR VARIABLES ---------------
salirPrograma = False
numerosDesordenados = []

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

# ------------ EJECUCIÓN PRINCIPAL ----------------
while salirPrograma == False:
    numerosDesordenados = []
    print('Bienvenido, vamos a ordenar tres números:')
    # Obtener y validar los datos ingresados.
    for x in range(3):
        numero = input('Escriba un número:')
        esValido = verificarTipoDato(numero, int)
        if esValido == True:
            numerosDesordenados.append(int(numero))
        else:
            print(f'El valor ingresado por teclado "{numero}", no es un valor númerico válido.')
            print('Deberá reiniciar el programa para capturar los datos correctos.')
            salirPrograma = True
            break
    # Ordenarlos números recibidos.
    numerosDesordenados.sort()
    if len(numerosDesordenados) == 3:
        print('Los números en orden ascendente son:')
        for n in numerosDesordenados:
            print(n)
    salirPrograma = continuarSiNo()