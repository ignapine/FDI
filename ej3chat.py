numero1 = (float(input("escoja un numero")))
numero2 = (float(input("escoja otro numero")))
numero3 = (float(input("escoja otro numero")))


if numero1 >= numero2 and numero1 >= numero3 :
    print("numero 1 es el mas grande de los tres numeros")

elif numero2 >= numero1 and numero2 >= numero3 :
    print("numero 2 es el mas grande de los tres numeros")

else:
    print("el numero 3 es el mas grande de los tres numeros")