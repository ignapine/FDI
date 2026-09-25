#Una empresa de tecnología desea desarrollar un sistema para gestionar los precios de
#venta de sus productos. El sistema debe solicitar el importe de 10 productos, y cada
#uno debe tener un precio entre $6,000 y $50,000. Si el precio está fuera de este
#rango, el sistema debe volver a solicitar un nuevo precio, indicando que el valor
#está fuera de rango.
#Al final, se debe generar un informe con la cantidad de productos y los importes
#totales en las siguientes categorías:
#Productos con precios entre $6,000 y $30,000 inclusive.
#Productos con precios mayores a $30,000 y menores a $40,000.
#Productos con precios mayores o iguales a $40,000.
#Para finalizar, imprimir: "Desarrollado por " + nombre del alumno.

while True:
    precio = float(input("Ingrese precio:"))

    if precio >= 6000 and precio <= 50000:
        break
    else:
        print("Precio fuera de rango")

articulo1 =