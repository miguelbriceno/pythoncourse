# Hallar el area de un circulo
import math
print('Hallar el areá de un circulo dado su radio.')
radio = float(input('Ingrese el radio del circulo: '))
area = math.pi * (radio**2)
print(f'El area del circulo es: {round(area, 2)}')