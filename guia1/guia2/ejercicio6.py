'''Se tiene como datos los sueldos de tres empleados: Suel1, Suel2, Suel3 y tres descuentos
variables expresados como porcentajes: Porc1, Porc2, Porc3, respectivamente. Calcular
y mostrar cada uno de los sueldos netos. '''

suel1 = float(input("Ingrese el sueldo del empleado 1: "))
porc1 = float(input("Ingrese el porcentaje de descuento 1: "))

suel2 = float(input("Ingrese el sueldo del empleado 2: "))
porc2 = float(input("Ingrese el porcentaje de descuento 2: "))

suel3 = float(input("Ingrese el sueldo del empleado 3: "))
porc3 = float(input("Ingrese el porcentaje de descuento 3: "))

neto1 = suel1 - (suel1 * (porc1 / 100))
neto2 = suel2 - (suel2 * (porc2 / 100))
neto3 = suel3 - (suel3 * (porc3 / 100))

print("Sueldo neto empleado 1: " , neto1)
print("Sueldo neto empleado 2: " , neto2)
print("Sueldo neto empleado 3: " , neto3)