#Ejercicio2
'''Ejercicio 2: Compra en supermercado
Crear un programa que:
* Pida la edad del cliente y el monto total de compra
* Determine si es menor de edad o mayor de edad
* Clasifique el tipo de compra:
o Alta: >= 10000
o Media: >= 5000
o Baja: < 5000
* Aplique beneficios:
o Si es mayor de edad y compra >= 10000: "Descuento del 15%"
o Si es menor de edad y compra >= 5000: "Descuento del 10%"
o Si compra < 5000: "Sin descuento"
'''

edad = int(input("Ingrese la edad:"))
monto = float(input("Ingrese el monto total de su compra: "))

if edad >=18 and monto>=10000:
    print("Es mayor de edad")
    print("Tipo de compra: alta")
    print("Tiene un descuento del 15%")
elif edad <18 and monto >= 5000:
    print("Es menor de edad")
    print("Tipo de compra: media")
    print("Tiene un descuento del 10%")
elif monto <5000:
    print("Tipo de compra: baja")
    print("Sin descuento")


