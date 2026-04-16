'''Sean N y M dos números naturales, escriba un algoritmo para determinar si N es
divisible por M '''

N = int(input("Ingrese el número N (dividendo): "))
M = int(input("Ingrese el número M (divisor): "))

if M != 0:
    if N % M == 0:
        print(f"{N} es divisible por {M}")
    else:
        print(f"{N} no es divisible por {M}")
else:
    print("No se puede dividir por cero.")

    #no entra en el parcial