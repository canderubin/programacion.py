#Un cliente realiza una compra en un supermercado y adquiere 3 productos. 
# Los precios son de $4500, $3200 y $2100. 
# El supermercado aplica un descuento del 10% sobre el total de la compra.
#Determinar cuánto deberá pagar el cliente luego del descuento.


producto1_ = int(input("Ingresar valor del producto 1: "))
producto2_ = int(input("Ingresar valor del producto 2: "))
producto3_ = int(input("Ingresar valor del producto 3: "))

total = producto1_ + producto2_ + producto3_
print(total)
descuento = (total/100) * 10
print(descuento)
pagar = total - descuento
print("El monto final a pagar es", pagar, sep=" --> $")

