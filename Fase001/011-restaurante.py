# Programa para calcular los descuentos en el restaurante.

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
        print('Si desea continuar usando el programa oprima "s", de lo contrario oprima "n" para salir.')
        eleccion = input()
        if eleccion == 'N' or eleccion == 'n':
            opcionElegida = True
        elif eleccion == 's' or eleccion == 'S':
            opcionElegida = False
        else:
            print(f'La tecla oprimida -{eleccion}- no es una opción elegible. La respuesta por defecto "Salir" se aplicará.')
            opcionElegida = True
    return opcionElegida

# Funcion 3 - Calcular descuento sobre consumoBase
def calcularDescuento(consumo):
    descuento = 0
    if consumo <= 100:
        descuento = consumo * 0.10
    elif consumo > 100 and consumo <= 200:
        descuento = consumo * 0.20
    else:
        descuento = consumo * 0.20
    return descuento

# Funcion 4 - Calcular impuesto
def calcularImpuesto(consumo):
    impuesto = 0
    impuesto = consumo * 0.19
    return impuesto

# ------------ EJECUCIÓN PRINCIPAL ----------------
while salirPrograma == False:
    # Ingreso datos
    print('Bienvenido, por favor ingrese el monto del consumo:')
    consumoBase = input()
    esValido = verificarTipoDato(consumoBase, float)
    if esValido == False:
        print('El dato ingresado debe ser una cantidad escrita en números.\nVolveremos a iniciar el programa:')
        continue
    else:
        consumoBase = abs(float(consumoBase))
        # Calcular descuento
        valorDescuento = calcularDescuento(consumoBase)
        # Calcular impuesto
        impuestoAplicado = calcularImpuesto((consumoBase - valorDescuento))
        # Calcular total
        total = (consumoBase - valorDescuento) + impuestoAplicado
    # Mostrar resultados
    print('-' * 20)
    print(f'Consumo..........{round(consumoBase, 2)}')
    print(f'Descuento........{round(valorDescuento, 2)}')
    print(f'Impuesto 19%.....{round(impuestoAplicado, 2)}')
    print('-' * 20)
    print('-' * 20)
    print(f'TOTAL..........{round(total, 2)}')
    print('-' * 20)
    print('\n')
    salirPrograma = continuarSiNo()