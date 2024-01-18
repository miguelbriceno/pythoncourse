# Programa para ...

# -------------- IMPORTACIÓN DE MÓDULOS -------------

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
        print('Si desea continuar con la ejecución oprima "s", de lo contrario oprima "n" para salir.')
        eleccion = input()
        if eleccion == 'N' or eleccion == 'n':
            opcionElegida = True
        elif eleccion == 's' or eleccion == 'S':
            opcionElegida = False
        else:
            print(f'La tecla oprimida -{eleccion}- no es una opción elegible. La respuesta por defecto "Salir" se aplicará.')
            opcionElegida = True
    return opcionElegida

# Funcion 3 - Conversor de moneda a dolares
def conversor(opcionElegida):
    # Si agrega más opciones la menú deberá agregar otro 'elif' en esta parte de funcion, definiendo las variables de forma que se ajusten a la opción agregada en el menú.
    # Validar que opción se envía desde main
    if opcionElegida == 0:
        return True
    elif opcionElegida == 1:
        moneda1 = 'COP'
        moneda2 = 'USD'
        tasaCambio = 3952.89
    elif opcionElegida == 2:
        moneda1 = 'USD'
        moneda2 = 'COP'
        tasaCambio = 3952.89
    else:
        print(f'Error001: La opción elegida {opcionElegida} no corresponde a una opción válida del menú.')
        return False
    # Solicitar y verificar datos de entrada
    total = input("Ingese la cantidad de dinero que desea convertir:")
    esValido = verificarTipoDato(total,float)
    # Calcular cambio
    if esValido == True:
        total = float(total)
        # Si agrega otra opción al menú también deberá agregar aqui un 'elif' extra que realize la operación de conversión añadida.
        if opcionElegida == 1:
            conversion = total / tasaCambio
            conversion = round(conversion, 2)
        elif opcionElegida == 2:
            conversion = total * tasaCambio
            conversion = round(conversion, 2)
        else:
            print(f'Error003: {opcionElegida} no corresponde a una opción del menú. Intente de nuevo.')
            return False
        return f'{total} {moneda1} son {conversion} {moneda2} '
    else:
        print("El valor en dinero que has ingresado es incorrecto, o no es un número, por favor intenta de nuevo.")
        return False


# Funcion 0 - FUNCIÓN PRINCIPAL
def main():
    #---------------- DECLARAR VARIABLES ---------------
    salirPrograma = False
    # Pude añadir opciones al menu si desea, pero deberá modicar la funcion # 3 de acuerdo a los cambios que desee.
    menu = """
    
    1- COP -> USD
    2- USD -> COP
    0- Salir

    """
    opcion = ''
    #----------------EJECUCIÓN INICIAL------------------
    while salirPrograma == False:
        # Solicitar y verifacar opción
        print('Programa conversor de moneda.\n')
        print(menu)
        opcion = input('Escriba el número de la opción que desee utilizar:')
        opcionValida = verificarTipoDato(opcion, int)
        if opcionValida == True:
            opcion = int(opcion)
            resultado = conversor(opcion)
        else:
            print(f'{opcion} no es una opción válida, intente nuevamente.')
        # Entrega de resultados
        if resultado == True:
            print(f'Elegiste la opción {opcion}, salir.')
            salirPrograma = True
            break
        elif resultado == False:
            print('Debido al error presentado, deberás intentar nuevamente.')
        else:
            print(f'{resultado}')
        salirPrograma = continuarSiNo()


# ------------ PUNTO DE ENTRADA DE LA APLICACIÓN ----------------
if __name__ == '__main__':
    main()