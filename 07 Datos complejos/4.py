# Crear diccionario vacío para almacenar los contactos
contactos = {}

# Cargar 5 contactos desde entrada del usuario
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero  # Guardar en el diccionario

# Consultar un contacto por nombre
consulta = input("Ingresá el nombre que querés consultar: ")

# Verificar si el nombre existe en el diccionario
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("Ese contacto no está registrado.")
