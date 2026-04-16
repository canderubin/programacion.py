'''Un cine cobra $3500 por entrada. Si una persona compra varias entradas, obtiene un descuento del 20% sobre el total.
Ingresar la cantidad de entradas y calcular cuánto deberá pagar.'''

entradaindividual =(3500)
entradas = int(input("Ingrese la cantidad de entradas a comprar: "))
totalentradas = (entradaindividual * entradas)
print("Costo de entradas" , totalentradas, sep=" -->")
descuento = (totalentradas/100) *20
print("El descuento es de:" , descuento , sep=" --> $")
totalpagar = (totalentradas - descuento)
print("El costo total a pagar es", totalpagar, sep=" --> $")