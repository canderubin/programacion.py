'''La idea es que, al ingresar la cantidad actual de productos de un determinado artículo, 
el sistema determine automáticamente cuál es la siguiente centena completa mayor.'''

articulo = input("Ingrese el articulo: ")
productos = int(input("Ingrese la cantidad de productos: "))

#Si el resto de dividir por 100 es distinto de 0 (sobran productos)
if productos % 100 != 0:
    #Calculo cuántas centenas hay 
    cantidadcentenas = productos // 100
    
    #Sumo una más para saltar a la que sigue 
    siguientecentena = cantidadcentenas + 1
    
    #Vuelvo a convertir en centenas 
    resultado = siguientecentena * 100
else:
    #Si el resto es 0, el resultado es el mismo número
    resultado = productos

print("El espacio a reservar es para:", resultado)