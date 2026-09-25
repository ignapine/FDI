nota1 = (float(input("nota 1 del estudiante")))
nota2 = (float(input("nota 2 del estudiante")))
nota3 = (float(input("nota 3 del estudiante")))

suma_de_las_notas = ((nota1 + nota2 + nota3)/3) 


print(suma_de_las_notas)

if suma_de_las_notas >= 6 :
    print("APROBADOOOOOOOOOOO")


if suma_de_las_notas < 6 : 
    print("desaprobado")
