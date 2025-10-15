# Solicitar una frase al usuario
frase = input("Ingresá una frase: ")

# Separar la frase en palabras usando el espacio como delimitador
palabras = frase.split()

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)

# Crear diccionario para contar ocurrencias
recuento = {}

# Recorrer cada palabra y contar cuántas veces aparece
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento de palabras:", recuento)
