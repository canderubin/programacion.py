'''Utilizando la estructura condicional simple. Realice un algoritmo que ingresando un número, 
muestre sólo un mensaje si el mismo es positivo.
Entrada: un número.
Salida: "Es positivo"'''

# Entrada de datos
entrada = input("Ingrese un número: ")

try:
    # Conversión a número decimal
    numero = float(entrada)
    
    # Condicional simple (solo evalúa si es verdadero)
    if numero > 0:
        print("Es positivo")

except:
    # Manejo de error si no se ingresa un número
    print("Los datos ingresados no son correctos")