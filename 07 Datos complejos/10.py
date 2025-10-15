# Diccionario original: país → capital
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

# Crear diccionario invertido: capital → país
capitales = {}

# Recorrer el diccionario original e invertir claves y valores
for pais, capital in paises.items():
    capitales[capital] = pais

# Mostrar el nuevo diccionario
print("Diccionario invertido (capital → país):")
print(capitales)
