# Programa para detectar si se ingresó una vocal o no.

#---------------- DECLARAR VARIABLES ---------------
salirPrograma = False

# --------------- DEFINIR FUNCIONES -----------------
# Funcion 1 - Verificar el tipo de dato para continuar
def verificarSiEsLetra(letra):
    abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if letra in abecedario:
        return True
    else:
        return False

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

# Funcion 3 - Evaluar si es vocal o consonante
def esVocalConsonante(caracter):
    vocales = ['a','e','i','o','u','A','E','I','O','U']
    if caracter in vocales:
        return True
    else:
        return False

# ------------ EJECUCIÓN PRINCIPAL ------------------
while salirPrograma == False:
    print('Bienvenido, escriba una letra del abecedario por favor.')
    caracterEvaluado = input()
    # Revisar si es un caracter
    if len(caracterEvaluado) > 1:
        print(f'"{caracterEvaluado}" no es un caracter, sino una cadena. No se puede evaluar.')
    else:
        esEvaluable = verificarSiEsLetra(caracterEvaluado)
    # Si es evaluable, revisar si es una vocal
    if esEvaluable == True:
        resultado = esVocalConsonante(caracterEvaluado)
        # Mostrar resultado del análisis
        if resultado == True:
            print(f'El caracter "{caracterEvaluado}" es una vocal')
        else:
            print(f'El caracter "{caracterEvaluado}" no es una vocal, es una consonante.')
    else:
        print(f'El caracter ingresado -"{caracterEvaluado}"- no es evaluable, ya que no es una letra del abecedario.')
    salirPrograma = continuarSiNo()