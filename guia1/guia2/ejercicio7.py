'''Dados dos nombres escritos en minúscula obtengo la longitud de cada uno de ellos.
Detallar tipo de datos de la entrada y de la salida. '''

# Entrada: nombre1 , nombre2 
nombre1 = input("Ingrese el primer nombre en minúscula: ")
nombre2 = input("Ingrese el segundo nombre en minúscula: ")

longitud1 = len(nombre1)
longitud2 = len(nombre2)

# Salida: longitud1 , longitud2 
print(f"El nombre {nombre1} tiene {longitud1} caracteres.")
print(f"El nombre {nombre2} tiene {longitud2} caracteres.") 