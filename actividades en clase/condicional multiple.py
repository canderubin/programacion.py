#Condicional multiple

edad = int(input("Ingrese su edad: "))


#CONDICIONAL DOBLE
if edad < 18:
    print("Es menor de edad")
elif edad >= 18 and edad <= 23 :
    print("Es estudiante de la UTN")
elif edad >= 23 and edad < 60 :
    print("Es profesor")
else:
    print("Es jubilado")

