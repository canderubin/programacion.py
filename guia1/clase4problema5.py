'''
En un restaurante, el cliente desea dejar una propina del 12% sobre el total consumido.
Si el monto total de la cuenta es ingresado por teclado, calcular el total a pagar incluyendo la propina.
'''

toltalconsumido = int(input("Ingrese el total consumido: "))
propina = (toltalconsumido/100) * 12
print(propina)
pagar = (toltalconsumido + propina)
print("El total a pagar es:", pagar, sep="$")