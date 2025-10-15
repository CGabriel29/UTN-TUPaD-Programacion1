# Crear diccionario vacío para la agenda
agenda = {}

# Cargar 3 eventos como ejemplo (podés cambiar la cantidad o hacerlo dinámico)
for i in range(3):
    dia = input(f"Ingresá el día del evento {i+1}: ")
    hora = input(f"Ingresá la hora del evento {i+1} (formato HH:MM): ")
    evento = input(f"¿Qué actividad hay el {dia} a las {hora}?: ")
    
    # Guardar el evento en la agenda con clave (día, hora)
    agenda[(dia, hora)] = evento

# Consultar una actividad por día y hora
consulta_dia = input("\nIngresá el día que querés consultar: ")
consulta_hora = input("Ingresá la hora que querés consultar (formato HH:MM): ")

# Verificar si existe un evento en ese momento
clave = (consulta_dia, consulta_hora)
if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay ninguna actividad registrada en ese horario.")
