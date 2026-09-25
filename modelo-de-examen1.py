def pedir_poliza():
    while True:
        precio = float(input("Ingrese el importe de la póliza: "))

        if precio >= 6000 and precio <= 50000:
            return precio
        else:
            print("Precio fuera de rango. Ingrese nuevamente.")


cantidad_1 = 0
importe_1 = 0

cantidad_2 = 0
importe_2 = 0

cantidad_3 = 0
importe_3 = 0


for i in range(10):

    precio = pedir_poliza()

    if precio >= 6000 and precio <= 30000:
        cantidad_1 += 1
        importe_1 += precio

    elif precio > 30000 and precio < 40000:
        cantidad_2 += 1
        importe_2 += precio

    elif precio >= 40000:
        cantidad_3 += 1
        importe_3 += precio


print("Pólizas entre $6000 y $30000:", cantidad_1)
print("Importe total:", importe_1)

print("Pólizas mayores a $30000 y menores a $40000:", cantidad_2)
print("Importe total:", importe_2)

print("Pólizas mayores o iguales a $40000:", cantidad_3)
print("Importe total:", importe_3)

print("Desarrollado por Ignacio")