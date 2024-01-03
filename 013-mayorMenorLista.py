# Programa para ingresar seis números en una lista y sacar el mayor y el menor

# -------------- IMPORTACIÓN DE MÓDULOS -------------
import random

#---------------- DECLARAR VARIABLES ----------------
salirPrograma = False
lista = []

# --------------- DEFINIR FUNCIONES -----------------
# Funcion 1 - Evaluadora de continuidad
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
    lista.clear()
    print('Los seis números se ingresaran de forma aleatoria entre 0 y 1000.\n')
    for x in range(6):
        numero = random.randrange(1000)
        lista.append(numero)
    # Obtener el mayor y el menor
    lista.sort()
    mayor = lista[-1]
    menor = lista[0]
    print(f'El número mayor es: {mayor}')
    print(f'El número menor es: {menor}')
    print('')
    print(f'La lista entera es: {lista}\n')
    salirPrograma = continuarSiNo()

'''
numeros = [int(input("Ingrese un numero: ")) for n in range(6)]

mayor = max(numeros)
menor = min(numeros)

print("El mayor de la lista es: ",mayor)
print("El menor de la lista es: ",menor)
'''