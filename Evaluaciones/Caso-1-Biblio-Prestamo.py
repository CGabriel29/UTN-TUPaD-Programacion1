# Listas paralelas
titulos = []
ejemplares = []

# Variable de control
opcion = 0

while opcion != 10:
    print("\nMENÚ DE LA BIBLIOTECA ESCOLAR")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo con stock")
    print("10. Salir")

    entrada = input("Seleccione una opción: ")
    if entrada.isdigit():
        opcion = int(entrada)
    else:
        print("Debe ingresar un número válido.")
        continue

    if opcion == 1:
        cantidad = int(input("¿Cuántos títulos desea ingresar? "))
        for i in range(cantidad):
            titulo = input("Título " + str(i+1) + ": ")
            titulos.append(titulo)
        print("Títulos cargados correctamente.")

    elif opcion == 2:
        if len(titulos) == 0:
            print("Primero debe ingresar los títulos (opción 1).")
        else:
            ejemplares.clear()  # Solo se borra ejemplares, no títulos
            for i in range(len(titulos)):
                copias = input("Ejemplares disponibles de '" + titulos[i] + "': ")
                if copias.isdigit():
                    ejemplares.append(int(copias))
                else:
                    print("Entrada inválida. Se asigna 0 por defecto.")
                    ejemplares.append(0)
            print("Ejemplares cargados correctamente.")

    elif opcion == 3:
        if len(titulos) == 0:
            print("No hay títulos cargados.")
        elif len(ejemplares) == 0:
            print("No hay ejemplares cargados.")
        elif len(titulos) != len(ejemplares):
            print("Las listas están desincronizadas. Verifique los datos.")
        else:
            print("\nCATÁLOGO CON STOCK:")
            for i in range(len(titulos)):
                print(titulos[i] + ": " + str(ejemplares[i]) + " copias")

    elif opcion == 10:
        print("Saliendo del sistema.")
    else:
        print("Opción inválida.")





