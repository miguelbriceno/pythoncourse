'''
# Convertir una cantidad dada de segundos en minutos y horas.

# Solicitar ingreso de datos:
segundos = int(input('Ingrese la cantidad de segundos: '))

# Converir a minutos
minutos = int(segundos / 60)

# Convertir a horas
horas = int(minutos / 60)

# Imprimir resultados
print(f'{segundos} segundos equivalen a {round(minutos, 1)} minutos, o lo que es igual a {round(horas, 1)} horas.')
'''
# Variables / Ingresar Datos
tiempoSegundos = input('Tiempo en Segundos: ')
HORA = 3600
MINUTO = 60

# Convertir de str a int
tiempoSegundos = int(tiempoSegundos)

# Solución 
h = tiempoSegundos // HORA
tiempoSegundos = tiempoSegundos % HORA
m = tiempoSegundos // MINUTO
s = tiempoSegundos % MINUTO

# Mostrar datos en pantalla 
print('Horas: ', h)
print('Minutos: ', m)
print('Segundos: ', s)