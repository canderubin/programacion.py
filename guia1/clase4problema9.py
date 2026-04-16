'''Una tienda vende camisetas a $8000 cada una.
Si el cliente compra más de 5, obtiene un descuento del 25% sobre el total.
Ingresar la cantidad de camisetas y calcular el monto final.
'''

valor = int(input("Ingrese el valor de una camiseta: "))
camiseta = int(input("Ingrese cantidad de camisetas a comprar: "))
preciototal = (valor * camiseta)
if camiseta > 5:
    descuento = (preciototal / 100) *25
    total = (preciototal - descuento)
    print("¡Tenes un descuento del 25%!")
    print("El total es:", total)
else: 
   montofinal = preciototal
   print("El total a pagar es:" , preciototal)