#El sistema del registro automotor, pide el desarrollo de un sistema que
#realice lo siguiente:
#Ingresar edades de personas mientras que la edad sea distinto de -1.
#El objetivo es calcular la cantidad de carnets de conducir, para pedir su impresión.
#Al finalizar se pide indicar la cantidad de personas mayores de 80 años,
#personas con edades entre 16 y 80 y personas menores de 16 años
#Para finalizar, imprimir: "desarrollado por " + nombre del alumno.

edad =(int(input("ingrese su edad ")))


if edad < 0 : 
    print(None)

if edad >= 80 :
    print("persona mayor a 80 anios")

elif edad < 80 and edad >= 16 :
    print("capacitada para manejar")

else:
    print("menor de edad para conducir")
    
