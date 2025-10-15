# Crear diccionario vacío para almacenar alumnos y sus notas
alumnos = {}

# Cargar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    
    # Solicitar 3 notas y convertirlas a enteros
    nota1 = int(input(f"Ingresá la primera nota de {nombre}: "))
    nota2 = int(input(f"Ingresá la segunda nota de {nombre}: "))
    nota3 = int(input(f"Ingresá la tercera nota de {nombre}: "))
    
    # Guardar las notas como tupla en el diccionario
    alumnos[nombre] = (nota1, nota2, nota3)

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
