'''Tres personas deciden invertir su dinero para formar una empresa. Cada una de ellas
invierte una cantidad distinta. Calcular y mostrar el porcentaje que cada una invierte con
respecto al total de la inversión. '''

inversion1 = float(input("Ingrese la inversión de la persona 1: "))
inversion2 = float(input("Ingrese la inversión de la persona 2: "))
inversion3 = float(input("Ingrese la inversión de la persona 3: "))

total = inversion1 + inversion2 + inversion3

porcentaje1 = (inversion1 / total) * 100
porcentaje2 = (inversion2 / total) * 100
porcentaje3 = (inversion3 / total) * 100

print(f"Persona 1 invirtió el {porcentaje1:.2f}% del total.")
print(f"Persona 2 invirtió el {porcentaje2:.2f}% del total.")
print(f"Persona 3 invirtió el {porcentaje3:.2f}% del total.")