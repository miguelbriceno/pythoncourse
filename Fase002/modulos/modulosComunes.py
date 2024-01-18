# 1) Evaluadora de continuidad
#-----------------------------------------
# Recibe un dato ingresado por el teclado y veriica que sea una de las opciones correctas (s,S,n,N). 
# Devuelve True si se elige salir del programa o si hay un error, y False si se eleige no salir del programa.
# ----------------------------------------
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


# 2) Verificar el tipo de dato para continuar
# ----------------------------------------
# Recibe un dato ingresado por telclado y el tipo de dato que se espera que sea, y retorna True si coincide o False si no coincide.
# ----------------------------------------
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
                print(f'Error000 - No se puede cambiar {datoIngresado} al tipo de dato {tipoBuscado}')
                break
    return tipoDatoIngresado