#Un empleado cobra un sueldo base mensual. Además, recibe un bono del 15% sobre su sueldo.
#Si el sueldo base es ingresado por teclado, determinar el sueldo final a cobrar.

sueldobase = int(input("Ingrese el valor de su sueldo: "))

bono = (sueldobase/100)*15
print(bono)
sueldototal = sueldobase + bono

print("El sueldo final es", sueldototal, sep=" --> $")