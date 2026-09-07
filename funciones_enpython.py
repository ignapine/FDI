#def sumar (a,b):
#    resultado = a+b
#    return (a+b)
#
#resultado = sumar(10,10)
#
#primt("la suma de 10 mas 10 es" +(resultado))
#


import math

area =float(input("dame un valor del area"))

def area_circulo(radio):
    area = math.pi * radio ** 2
    return area

print(area_circulo(area))
