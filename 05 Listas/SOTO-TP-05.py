# Ejercicio 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

# Ejercicio 2: Crear una lista con cinco elementos y mostrar el penúltimo
favoritos = ['Python', 'Café', 'Montaña', 'Libros', 'Música']
print(favoritos[-2])  # Muestra el penúltimo elemento: 'Libros'

# Ejercicio 3: Crear una lista vacía, agregar tres palabras con append e imprimir la lista
lista_vacia = []
lista_vacia.append("Python")
lista_vacia.append("Lógica")
lista_vacia.append("Algoritmos")
print(lista_vacia)

# Ejercicio 4: Reemplazar el segundo y último valor de la lista “animales”
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"      # Segundo elemento (índice 1)
animales[-1] = "oso"      # Último elemento (índice -1)
print(animales)

# Ejercicio 5: Analizar el siguiente programa y explicar qué realiza
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#Este programa crea una lista llamada numeros con cinco valores. Luego:
#Calcula el valor máximo de la lista usando max(numeros) → en este caso, 22.
#Elimina ese valor máximo con numeros.remove(...).
#Imprime la lista resultante, que ya no contiene el número más grande.

# Ejercicio 6: Crear una lista del 10 al 30 con saltos de 5 y mostrar los dos primeros elementos
numeros = list(range(10, 31, 5))
print(numeros[:2])  # Muestra los dos primeros: [10, 15]

# Ejercicio 7: Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos”
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "camioneta"   # Reemplaza "polo"
autos[2] = "coupe"       # Reemplaza "suran"
print(autos)

# Ejercicio 8: Crear una lista vacía y agregar el doble de 5, 10 y 15 usando append
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# Ejercicio 9: Modificar la lista "compras" según las instrucciones
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente (índice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en el segundo cliente (índice 1)
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente (índice 0)
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)

# Ejercicio 10: Crear una lista anidada con los elementos especificados
lista_anidada = [
    15,                # lista_anidada[0]
    True,              # lista_anidada[1]
    [25.5, 57.9, 30.6],# lista_anidada[2][0], [2][1], [2][2]
    False              # lista_anidada[3]
]

print(lista_anidada)
