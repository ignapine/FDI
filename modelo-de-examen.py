#Una empresa de venta de productos en forma mayorista, tiene un sistema de facturación,
#necesita realizar un cambio en el sistema, se pide proporcionar un algoritmo en
#Python que pida ingresar por teclado el precio_descuento de venta, luego indicar el precio_descuento
#con descuento, para precio_descuento mayores a 30000 del 5%, para precio_descuento mayores a $20000 del
#2% , si el precio_descuento de venta es menor, indicar que no tiene descuento.
#Para finalizar, imprimir: "desarrollado por " + nombre del alumno.

#precio_descuento de mas de 30000 se le pone 5% de descuento 
#precio_descuento de mas de 20000 se le pone 2% de descuento 
#si el precio_descuento es menor a 20000 no descuento 
print("si tu producto sale mas que 30000 5% de descuento pero si tu prod va de 20000 a 30000 2% y sino no descuento")
precio_descuento = (float(input("precio_descuento del producto :")))



if precio_descuento > 30000 :
       print = ("el descuento sera de ",(precio_descuento * 0.05))
    

elif precio_descuento >= 20000 :
        print = ("el descuento sera de ",(precio_descuento * 0.02))

else : 
    print("no hay descuento")

