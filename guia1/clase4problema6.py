'''Se desea convertir una temperatura ingresada en grados Celsius a grados Fahrenheit.
La fórmula es:
F = (C × 9/5) + 32
Mostrar el resultado.
'''

temperaturacelsius = int(input("Ingrese los grados Celsius: ")) #c= grados celsius
conversion = (temperaturacelsius * 9/5) + 32
print(conversion)
print("La conversion a Fahrenheit es: ", conversion, sep=" --> ")