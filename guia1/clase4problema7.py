'''Un producto tiene un precio base. Se debe calcular el precio final con IVA del 21%.
El precio base debe ser ingresado por el usuario.
'''
preciobase = int(input("Ingrese el precio base: ")) 
IVA = (preciobase / 100) * 21
print(IVA)
preciofinal = (preciobase + IVA)
print("El precio final es: ", preciofinal, sep="$")
