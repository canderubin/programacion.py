'''Un trabajador cobra $2500 por hora.
Si el usuario ingresa la cantidad de horas trabajadas, calcular el sueldo total.
'''
hora = int(input("Ingrese cuanto cobra por hora: "))
horastrabajadas = int(input("Ingrese las horas trabajadas: ")) 
total = (hora * horastrabajadas) 
print("Sueldo total: ", total , sep="$")