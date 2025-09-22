# Actividad 1: Solicitar la edad del usuario y mostrar si es mayor de edad

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")

# Actividad 2: Solicitar la nota del usuario y mostrar si está aprobado o desaprobado

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Actividad 3: Solicitar un número y verificar si es par usando el operador módulo (%)

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

# Actividad 4: Solicitar la edad del usuario y clasificarla en categorías

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Actividad 5: Solicitar una contraseña y verificar que tenga entre 8 y 14 caracteres (inclusive)

contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Actividad 6: Generar una lista de 50 números aleatorios entre 1 y 100,
# calcular su moda, mediana y media, y determinar si hay sesgo en la distribución.

import random
from statistics import mode, median, mean

# Generar lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular medidas estadísticas
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Mostrar resultados
print("Lista de números aleatorios:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)

# Evaluar sesgo
if moda < mediana < media:
    print("Distribución con sesgo positivo (a la derecha).")
elif moda > mediana > media:
    print("Distribución con sesgo negativo (a la izquierda).")
else:
    print("Distribución aproximadamente simétrica o sin sesgo claro.")

# Actividad 7: Solicitar una frase o palabra al usuario.
# Si termina con vocal, añadir un signo de exclamación al final; si no, imprimirla tal cual.

texto = input("Ingrese una frase o palabra: ")

# Verificamos si el último carácter es una vocal (minúscula o mayúscula)
if texto[-1].lower() in "aeiou":
    texto += "!"
    
print(texto)

# Actividad 8: Solicitar al usuario su nombre y una opción (1, 2 o 3) para transformar el texto.
# 1 → Mayúsculas (upper), 2 → Minúsculas (lower), 3 → Primera letra mayúscula (title)

nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida.")

# Actividad 9: Solicitar al usuario la magnitud de un terremoto y clasificarla según la escala de Richter

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

# Actividad 10: Solicitar hemisferio, mes y día al usuario, y determinar la estación del año correspondiente.

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
mes = int(input("Ingrese el mes (1 a 12): "))
dia = int(input("Ingrese el día (1 a 31): "))

# Convertimos la fecha en un número para facilitar la comparación (formato MMDD)
fecha = mes * 100 + dia

# Definimos los rangos de fecha para cada estación
if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif 321 <= fecha <= 620:
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif 621 <= fecha <= 920:
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif 921 <= fecha <= 1220:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = "Fecha inválida"
    estacion_sur = "Fecha inválida"

# Mostrar estación según hemisferio
if hemisferio == "N":
    print("Estación en el hemisferio norte:", estacion_norte)
elif hemisferio == "S":
    print("Estación en el hemisferio sur:", estacion_sur)
else:
    print("Hemisferio inválido. Use 'N' para norte o 'S' para sur.")
