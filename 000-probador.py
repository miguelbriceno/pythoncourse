valor1 = int(input('Número inicial: '))
valor2 = int(input('Número final: '))
valor2 += 1
cantidadPositivos = 0
cantidadNegativos = 0

# Solución
for numero in range(valor1, valor2):
    if numero % 2 == 0 :
        cantidadPositivos += 1  
    else:
        cantidadNegativos += 1


# Mostrar Datos
print('Cantidad POSITIVOS: ', cantidadPositivos)
print('Cantidad NEGATIVOS: ', cantidadNegativos)