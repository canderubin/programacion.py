'''Dado un vehículo de cuatro ruedas; cada una con un radio de cincuenta centímetros, 
calcular e imprimir cuántas vueltas dará cada rueda para desplazarse un kilómetro.
Tener en cuenta que la salida solo mostrará las vueltas enteras que realiza'''

import math

radio = int(input())

vueltas = int(100000 / (2 * math.pi * radio))

print(vueltas)