# Ejercicio 1: Imprimir los números enteros del 0 al 100, uno por línea

for numero in range(101):
    print(numero)
# Ejercicio 2: Solicita un número entero y determina cuántos dígitos contiene

numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print("El número tiene", cantidad_digitos, "dígito(s).")

# Ejercicio 3: Sumar todos los números enteros entre dos valores dados, excluyendo los extremos

inicio = int(input("Ingrese el primer valor: "))
fin = int(input("Ingrese el segundo valor: "))

# Aseguramos que inicio sea menor que fin
if inicio > fin:
    inicio, fin = fin, inicio

suma = 0
for numero in range(inicio + 1, fin):
    suma += numero

print("La suma de los números entre", inicio, "y", fin, "es:", suma)

# Ejercicio 4: Sumar números ingresados por el usuario hasta que se ingrese un 0

total = 0
numero = int(input("Ingrese un número entero (0 para terminar): "))

while numero != 0:
    total += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))

print("La suma total acumulada es:", total)

# Ejercicio 5: Juego de adivinanza de número entre 0 y 9

import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinanza = -1  # Valor inicial distinto para entrar al bucle

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

print("¡Correcto! El número era", numero_secreto)
print("Cantidad de intentos:", intentos)

# Ejercicio 6: Imprimir todos los números pares entre 0 y 100 en orden decreciente

for numero in range(100, -1, -2):
    print(numero)

# Ejercicio 7: Calcular la suma de todos los números entre 0 y un número entero positivo dado

limite = int(input("Ingrese un número entero positivo: "))

# Validación básica
if limite < 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    for numero in range(1, limite):
        suma += numero
    print("La suma de los números entre 0 y", limite, "es:", suma)

# Ejercicio 8: Ingresar 100 números enteros y contar pares, impares, positivos y negativos

cantidad = 100  # Cambiar este valor para pruebas con menos números

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResumen:")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

# Ejercicio 9: Calcular la media de 100 números enteros ingresados por el usuario

cantidad = 100  # Cambiar este valor para pruebas con menos números

suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

media = suma / cantidad
print("La media de los", cantidad, "números ingresados es:", media)


# Ejercicio 10: Invertir el orden de los dígitos de un número ingresado por el usuario

numero = int(input("Ingrese un número entero: "))
invertido = str(abs(numero))[::-1]  # Inversión de los dígitos

# Si el número era negativo, se conserva el signo
if numero < 0:
    invertido = "-" + invertido

print("Número invertido:", invertido)
