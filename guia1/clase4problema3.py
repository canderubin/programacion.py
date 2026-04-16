'''Un vehículo consume cierta cantidad de litros de combustible en un viaje. El precio del litro de nafta es de $980.
Si el usuario ingresa la cantidad de litros consumidos, calcular el costo total del viaje.'''

litrosconsummidos = int(input("Ingrese la cantidad de litros consumidos: "))
costo = (litrosconsummidos * 980)
print("El costo total del viaje es", costo, sep=" --> $")