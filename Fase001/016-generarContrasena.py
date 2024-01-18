# Programa para generar contraseñas seguras

# -------------- IMPORTACIÓN DE MÓDULOS -------------
import random

# --------------- DEFINIR FUNCIONES -----------------

# Funcion 1 - Evaluadora de continuidad
def continuarSiNo():
    opcionElegida = ''
    while opcionElegida == '':
        print('Si desea generar otra contraseña "s", de lo contrario oprima "n" para salir.')
        eleccion = input()
        if eleccion == 'N' or eleccion == 'n':
            opcionElegida = True
        elif eleccion == 's' or eleccion == 'S':
            opcionElegida = False
        else:
            print(f'La tecla oprimida -{eleccion}- no es una opción elegible. La respuesta por defecto "Salir" se aplicará.')
            opcionElegida = True
    return opcionElegida

# Funcion 2 - Generar contraseña
def generarContrasena():
    # Creación de lsita
    mayus = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    mins = []
    simbols =['*','.','-','!','$','%','&','-']
    for x in mayus:
        x = x.lower()
        mins.append(x)
    listaFinal = mayus + mins + simbols + numeros
    contrasena = []
    # Este for elige aleatoriamente los caracteres para formar la contraseña
    for i in range(15):
        char = random.choice(listaFinal)
        contrasena.append(char)
    # Se convierte a string y se retorna
    contrasena = ''.join(contrasena)
    return contrasena

# Funcion 0 - FUNCIÓN PRINCIPAL
def main():
    #---------------- DECLARAR VARIABLES ---------------
    salirPrograma = False
    #----------------EJECUCIÓN INICIAL------------------
    while salirPrograma == False:
        print('Este es un generador de contraseñas automático, esta es su contraseña sugerida:')
        print(generarContrasena())
        salirPrograma = continuarSiNo()


# ------------ PUNTO DE ENTRADA DE LA APLICACIÓN ----------------
if __name__ == '__main__':
    main()