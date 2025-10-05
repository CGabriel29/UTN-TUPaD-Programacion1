#En el siguiente programa para rendir una prueba de programacion, se me prohibe exclusivamente que no use try-except 
#como puedo quitarlo y que el codigo quede igualmente funcional?


# Inicialización de listas paralelas
titulos = []
ejemplares = []

# Variable de control para el menú
opcion = 0

# Bucle principal del menú
while opcion != 8:
    print("\nMENÚ DE LA BIBLIOTECA ESCOLAR")
    print("1. Ingresar lista de títulos")
    print("2. Ingresar lista de ejemplares disponibles")
    print("3. Mostrar catálogo con stock")
    print("4. Consultar disponibilidad de un título específico")
    print("5. Listar títulos agotados (0 ejemplares)")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        continue

    match opcion:
        case 1:
            titulos = []
            ejemplares = []
            cantidad = int(input("¿Cuántos títulos desea ingresar? "))
            for i in range(cantidad):
                titulo = input("Ingrese el título " + str(i+1) + ": ")
                titulos.append(titulo)
            print("Títulos cargados correctamente.")
        case 2:
             if len(titulos) == 0:
                print("Primero debe ingresar los títulos (opción 1).")
             else:
                ejemplares = []
                for i in range(len(titulos)):
                    try:
                        cantidad = int(input("Ejemplares disponibles de '" + titulos[i] + "': "))
                        if cantidad < 0:
                            cantidad = 0
                    except ValueError:
                        cantidad = 0
                    ejemplares.append(cantidad)
                print("Ejemplares cargados correctamente.")  
        case 3:
            if len(titulos) == 0:
                print("No hay títulos cargados. Use la opción 1.")
            elif len(ejemplares) == 0:
                print("No hay ejemplares cargados. Use la opción 2.")
            elif len(titulos) != len(ejemplares):
                print("Las listas están desincronizadas. Verifique los datos.")
                print("Títulos cargados: " + str(len(titulos)))
                print("Ejemplares cargados: " + str(len(ejemplares)))
            else:
                print("\nCATÁLOGO CON STOCK")
                for i in range(len(titulos)):
                    print(titulos[i] + ": " + str(ejemplares[i]) + " copias")
        case 4:
            consulta = input("Ingrese el título a consultar: ")
            if consulta in titulos:
                indice = titulos.index(consulta)
                if indice < len(ejemplares):
                    print("'" + consulta + "': " + str(ejemplares[indice]) + " copias disponibles")
                else:
                    print("No hay ejemplares registrados para ese título.")
        case 5:
            if len(titulos) == 0 or len(ejemplares) == 0:
                print("No hay datos cargados.")
            elif len(titulos) != len(ejemplares):
                print("Las listas están desincronizadas. Verifique los datos.")
            else:
                print("\nTÍTULOS AGOTADOS")
                hay_agotados = False
                for i in range(len(titulos)):
                    if ejemplares[i] == 0:
                        print("- " + titulos[i])
                        hay_agotados = True
                if not hay_agotados:
                    print("No hay títulos agotados.")
        case 6:
            nuevo_titulo = input("Ingrese el nuevo título: ")
            try:
                nuevas_copias = int(input("Ingrese la cantidad de ejemplares: "))
                if nuevas_copias < 0:
                    nuevas_copias = 0
            except ValueError:
                nuevas_copias = 0
            titulos.append(nuevo_titulo)
            ejemplares.append(nuevas_copias)
            print("'" + nuevo_titulo + "' agregado con " + str(nuevas_copias) + " copias.")        
        case 7:
            titulo_modificar = input("Ingrese el título a actualizar: ")
            if titulo_modificar in titulos:
                indice = titulos.index(titulo_modificar)
                if indice < len(ejemplares):
                    accion = input("¿Préstamo (P) o Devolución (D)? ").upper()
                    if accion == "P":
                        if ejemplares[indice] > 0:
                            ejemplares[indice] -= 1
                            print("Préstamo registrado.")
                        else:
                            print("No hay ejemplares disponibles para préstamo.")
                    elif accion == "D":
                        ejemplares[indice] += 1
                        print("Devolución registrada.")
                    else:
                        print("Acción no válida.")
                else:
                    print("No hay ejemplares registrados para ese título.")
            else:
                print("Título no encontrado.")    
        case 8:
            print("Saliendo del sistema. Gracias por usar la biblioteca.")
        case _:
            print("Opción inválida. Intente nuevamente.")    
            
            