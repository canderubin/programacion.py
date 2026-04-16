'''Dado un número natural N, se quiere obtener un número real R que sea el resultado de
dividir la suma de los dígitos de N por la cantidad de dígitos que posee N. Por ejemplo:
Si N = 3421 luego R = 10/4 = 2.5 '''

# Leer número (ejemplo: 83241)
N = int(input("Ingrese un número de 5 dígitos: "))

# Obtener cada dígito
d5 = N % 10
d4 = (N // 10) % 10
d3 = (N // 100) % 10
d2 = (N // 1000) % 10
d1 = (N // 10000) % 10

# Sumar dígitos
suma = d1 + d2 + d3 + d4 + d5

# Mostrar resultados
print("Dígitos:", d1, d2, d3, d4, d5)
print("Suma:", suma)