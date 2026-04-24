#Condicional doble

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
sueldo = float(input("Ingrese su sueldo: "))
descuento = float(input("Ingrese su descuento: "))

#CONDICIONAL DOBLE
if edad < 18:
    print("El cliente tiene menos de 18 años")
else:
    print("El cliente es mayor de 18 años" )

total = (sueldo*descuento)/100
print("El total del sueldo es: ",total)