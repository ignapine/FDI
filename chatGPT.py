import pandas as ps
# Datos de algunos estudiantes
datos = {
    "Nombre": ["Nacho", "Juan", "Sofia", "Martina", "Lucas"],
    "Edad": [18, 19, 18, 20, 19],
    "Nota": [8, 6, 9, 7, 4]
}

# Convertimos los datos en una tabla
df = ps.DataFrame(datos)

print("TABLA COMPLETA:")
print(df)

print("\n-------------------")

# Mostrar solamente los estudiantes que aprobaron
aprobados = df[df["Nota"] >= 6]

print("ESTUDIANTES APROBADOS:")
print(aprobados)

print("\n-------------------")

# Promedio de las notas
promedio = df["Nota"].mean()

print("PROMEDIO:")
print(promedio)

print("\n-------------------")

# Estudiante con la nota más alta
mejor = df.loc[df["Nota"].idxmax()]

print("MEJOR NOTA:")
print(mejor)

# Crear un array
notas = np.array([7, 8, 6, 9, 10])

print("Notas:", notas)

# Operaciones matemáticas
print("Suma:", np.sum(notas))
print("Promedio:", np.mean(notas))
print("Nota más alta:", np.max(notas))
print("Nota más baja:", np.min(notas))

# Operaciones sobre TODOS los elementos
notas_finales = notas + 1

print("Notas + 1:", notas_finales)

# Filtrar datos
aprobados = notas[notas >= 7]

print("Notas aprobadas:", aprobados)

import matplotlib.pyplot as plt

# Datos
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
ventas = [120, 150, 180, 130, 200, 250]

# Crear gráfico
plt.plot(meses, ventas, marker="o")

# Título y nombres de los ejes
plt.title("Ventas durante el año")
plt.xlabel("Mes")
plt.ylabel("ventas")

# Mostrar cuadrícula
plt.grid()

# Mostrar gráfico
plt.show()

x = np.arange(1, 11)
y = x ** 2

plt.plot(x, y, marker="o")

plt.title("Números al cuadrado")
plt.xlabel("Número")
plt.ylabel("Resultado")

plt.grid()
plt.show()