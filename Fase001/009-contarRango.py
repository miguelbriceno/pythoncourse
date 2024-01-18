# Programa para devolver la cantidad de números enteros en un rango

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
        print('Si desea ingresar otros números oprima "s", de lo contrario oprima "n" para salir.')
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
    misLimites = []
    listaConteo = []
    # Obtener y validar datos de ingreso
    print('Bienvenido, a continuación escriba primer número:')
    numeroInicial = input()
    inicialEsViable = verificarTipoDato(numeroInicial, int)
    print('Ahora escriba el segundo número:')
    numeroFinal = input()
    finallEsViable = verificarTipoDato(numeroFinal, int)
    # Si los datos son válidos, generar el rango y contar
    if inicialEsViable == True and finallEsViable == True:
        # Ordenarlos de menor a mayor por si acaso
        misLimites.append(int(numeroFinal))
        misLimites.append(int(numeroInicial))
        misLimites.sort()
        # Usar FOR para crear una lista con el rango
        for x in range(misLimites[0], misLimites[1]):
            listaConteo.append(x)
        # Contar la cantidad de elementos en la lista
        print(f'El rango definido fue de {misLimites[0]} a {misLimites[1]}, entre los cuales hay {len(listaConteo)} items.')
    else:
        print('Alguno de los datos ingresados no es correcto, recuerda usar solo enteros.\nVoelveremos a iniciar la aplicación.\n')
        continue
    salirPrograma = continuarSiNo()