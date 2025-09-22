# Gestión de turnos por especialidad médica
# Listas paralelas: especialidades[] y cupos[]
# Implementación sin funciones, con match-case

especialidades = []
cupos = []

while True:
    print("\nMENÚ PRINCIPAL")
    print("1. Ingresar lista de especialidades")
    print("2. Ingresar lista de cupos disponibles")
    print("3. Mostrar agenda")
    print("4. Consultar cupos de una especialidad")
    print("5. Listar especialidades sin cupo")
    print("6. Agregar especialidad")
    print("7. Ver sin cupo")
    print("8. Actualizar cupos (reservar/cancelar)")
    print("9. Ver agenda completa")
    print("10. Salir")

    opcion = input("Seleccione una opción (1-10): ")

    match opcion:
        case "1":
            print("\n--- Ingreso de especialidades ---")
            while True:
                nombre = input("Ingrese el nombre de la especialidad (o 'fin' para terminar): ").strip()
                if nombre.lower() == "fin":
                    break
                if nombre == "":
                    print("El nombre no puede estar vacío.")
                elif nombre in especialidades:
                    print("La especialidad ya existe.")
                else:
                    especialidades.append(nombre)
                    print("Especialidad agregada.")

        case "2":
            print("\n--- Ingreso de cupos por especialidad ---")
            if len(especialidades) == 0:
                print("Primero debe ingresar especialidades.")
            else:
                cupos.clear()
                for esp in especialidades:
                    while True:
                        entrada = input(f"Ingrese cupos disponibles para '{esp}': ")
                        if entrada.isdigit():
                            cupos.append(int(entrada))
                            break
                        else:
                            print("Ingrese un número entero válido.")

        case "3":
            print("\n--- Agenda de especialidades ---")
            if len(especialidades) == 0:
                print("No hay especialidades registradas.")
            else:
                for i in range(len(especialidades)):
                    print(f"{especialidades[i]}: {cupos[i]} cupos")

        case "4":
            print("\n--- Consulta de cupos ---")
            nombre = input("Ingrese el nombre de la especialidad: ").strip()
            if nombre in especialidades:
                i = especialidades.index(nombre)
                print(f"{nombre}: {cupos[i]} cupos disponibles")
            else:
                print("Especialidad no encontrada.")

        case "5" | "7":
            print("\n--- Especialidades sin cupo ---")
            hay_vacias = False
            for i in range(len(especialidades)):
                if cupos[i] == 0:
                    print(f"{especialidades[i]}: sin cupos")
                    hay_vacias = True
            if not hay_vacias:
                print("Todas las especialidades tienen cupos disponibles.")

        case "6":
            print("\n--- Agregar nueva especialidad ---")
            nombre = input("Ingrese el nombre de la nueva especialidad: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")
            elif nombre in especialidades:
                print("La especialidad ya existe.")
            else:
                while True:
                    entrada = input(f"Ingrese cupos iniciales para '{nombre}': ")
                    if entrada.isdigit():
                        especialidades.append(nombre)
                        cupos.append(int(entrada))
                        print("Especialidad agregada.")
                        break
                    else:
                        print("Ingrese un número entero válido.")

        case "8":
            print("\n--- Actualizar cupos ---")
            nombre = input("Ingrese la especialidad: ").strip()
            if nombre not in especialidades:
                print("Especialidad no encontrada.")
            else:
                i = especialidades.index(nombre)
                print(f"Cupos actuales para {nombre}: {cupos[i]}")
                accion = input("¿Desea reservar (R) o cancelar (C) una cita?: ").strip().upper()
                if accion not in ["R", "C"]:
                    print("Opción inválida.")
                else:
                    cantidad = input("Ingrese la cantidad: ")
                    if not cantidad.isdigit():
                        print("Debe ingresar un número entero.")
                    else:
                        cantidad = int(cantidad)
                        if accion == "R":
                            if cantidad <= 0:
                                print("La cantidad debe ser mayor que cero.")
                            elif cantidad > cupos[i]:
                                print("No hay suficientes cupos disponibles.")
                            else:
                                cupos[i] -= cantidad
                                print("Cupo actualizado.")
                        else:
                            if cantidad < 1:
                                print("La cantidad debe ser mayor o igual a 1.")
                            else:
                                cupos[i] += cantidad
                                print("Cupo actualizado.")

        case "9":
            print("\n--- Agenda completa ---")
            print("Horario de atención: 08:00 a 18:00")
            for i in range(len(especialidades)):
                print(f"{especialidades[i]}: {cupos[i]} cupos")

        case "10":
            print("Programa finalizado.")
            break

        case _:
            print("Opción inválida. Intente nuevamente.")
