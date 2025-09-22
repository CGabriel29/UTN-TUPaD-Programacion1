# Caso 1 - Bliblioteca escolar - Prestamos de libros

# Inicializacion de listas paralelas

titulos = []
ejemplares = []

opcion = 0

# Menu
while opcion != 10:
    print ("\nMENU DE BIBLIOTECA ESCAOLAR")
    print("1. Ingresar lista de titulos")
    print("2. Ingresar lista de ejmplares disponibles")
    print("3. Mostrar catalogo en stock")
    print("4. Consultar disponibilidad de un titulo especifico")
    print("5. Listar titulos agotados (0 ejemplares)")
    print("6. Agregar titulo")
    print("7. Ver titulos agotados")
    print("8. Actualizar Ejmplares (prestamo/devolucion)")
    print("9. Ver catalogo")
    print("10. Salir")
    
    try:
        opcion = int (input("Seleccine una opcion: "))
    except ValueError:
        print("Ingrese un número valido.")
        continue
    
    match opcion:
        case 1:
            titulos = []
            ejemplares = []
            cantidad = int(input("¿Cuantos titulos desea ingresar? "))
            for i in range (cantidad):
                titulo = input("Ingrese el titulo "+ str(i+1)+": ")
                titulos.append(titulo)
            print("Titulos cargados correctamente.")
        
        case 2:
            if len(titulos) == 0:
                print("Primero debe ingresar los titulos (opcion 1).")
            else:
                ejemplares = []
                for i in range(len(titulos)):
                    try:
                        cantidad = int (input("Ejemplares disponibles de "+ titulos[i]+": "))
                        if cantidad < 0:
                            cantidad = 0
                    except ValueError:
                        cantidad = 0
                    ejemplares.append(cantidad)
        
        case 3:
            if len(titulos) == 0:
                print("No hay Titulos cargados. Use la opcion 1.")
            elif len(ejemplares)==0:
                print("No hay ejemplares cargados. Use la opcion 2.")
            elif len(titulos) != len(ejemplares):
                print("Las listas estan desincronizadas. Verifique los datos: ")
                print("Titulos cargados: "+str(len(titulos)))
                print("Ejemplares cargados: "+str(len(ejemplares)))
            else:
                print("\nCATALOGO CON STOCK")
                for i in range(len(titulos)):
                    print(titulos[i]+": "+str(ejemplares[i])+" copias")
        
        case 4:
            consulta = input("Ingrese el título a consultar: ").strip().lower()
            encontrado = False

            for i in range(len(titulos)):
                if titulos[i].lower() == consulta:
                    if i < len(ejemplares):
                       if ejemplares[i] == 0:
                          print("'" + titulos[i] + "' está agotado (0 copias disponibles)")
                       else:
                         print("'" + titulos[i] + "': " + str(ejemplares[i]) + " copias disponibles")
                    else:
                       print("No hay ejemplares registrados para ese título.")
                    encontrado = True
                    break

            if not encontrado:
                 print("Título no encontrado en el catálogo.")
        
        case 5|7:
            if len(titulos) == 0 or len (ejemplares) == 0:
                print("No hay datos cargados. ")
            elif len(titulos) != len(ejemplares):
                print("Las listas estan desincronizadas. Verifique los datos.")
            else: 
                print("\nTITULOS AGOTADOS")
                hay_agotados = False
                for i in range(len(titulos)):
                    if ejemplares[i] == 0:
                        print("- " + titulos[i])
                        hay_agotados = True
                if not hay_agotados:
                    print("No hay titulos agotados")
        
        case 6: 
            nuevo_titulo = input("Ingrese el nuevo titulo: ")
            try:
                 nuevas_copias = int(input("Ingrese la cantidad de ejemplares: "))
                 if nuevas_copias < 0:
                     nuevas_copias=0
            except ValueError:
                nuevas_copias=0
            titulos.append(nuevo_titulo)
            ejemplares.append(nuevas_copias)
            print("'" + nuevo_titulo + "' agregado con " + str(nuevas_copias)+ " copias. ")
        
        case 8:
            titulo_modificar = input ("Ingrese el titulo a actualizar: ")
            if titulo_modificar in titulos:
                indice = titulos.index(titulo_modificar)
                if indice < len(ejemplares):
                    accion = input("Prestamo (P) ó Devolucion (D)? ").upper()
                    if accion == "P":
                            if ejemplares[indice] > 0:
                                ejemplares[indice] -= 1
                                print("Prestamo registrado.")
                            else:
                                print("No hay ejemplares disponibles para prestamo. ")
                    elif accion == "D":
                        ejemplares[indice] += 1
                        print("Devolucion registrada. ")
                    else:
                        print("Accion no valida. ")
                else: 
                    print("No hay ejemplares registrados para ese titulo.")
            else:
                print("Titulo no encontrado. ")
        
        case 9:
            if len(titulos) == 0:
                print("No hay titulos cargados. ")
            else:
                print("\nCATALOGO COMPLETO")
                for i in range(len(titulos)):
                    print("- " + titulos [i])
        
        case 10:
            print("Saliendo del sistema. Gracias por usar la biblioteca. ")
        
        case _:
            print("Opcion invalida. Intente nuevamente. ")               