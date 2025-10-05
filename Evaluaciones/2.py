# Caso 2 Clínica — Turnos por especialidad (cupos del día)

especialidades = ["Cardiología", "Dermatología", "Pediatría"]
cupos = [5, 0, 10]

# Menu principal
while True:
    print("::::::::::::::::::::::::::::::::::")
    print("          MENU PRINCIPAL             ")
    print("1. Ingresar lista de especialidades")
    print("2. Ingresar lista de cupos disponibles")
    print("3. Mostrar agenda")
    print("4. Consultar cupos")
    print("5. Listar especialidades sin cupos")
    print("6. Agregar especialidad")
    print("7. Actualizar cupos (reservar/cancelar)")
    print("8. Listar especialidades")
    print("9. Salir")
    print("::::::::::::::::::::::::::::::::::")
    
    opcion = input("Seleccione una opcion: ")
    
    '''if not opcion.isdigit():
        print("Error. Ingrese un numero valido.")
        continue
    opcion = int(opcion)'''
    
    match opcion:
        case '1':
            # Agregar Especialidades nuevas sin cupos establecidos
            cant = input("Cuantas especialidades desea agregar?--> ")
            
            #Verificacion necesaria
            if not cant.isdigit():
               print("Error. Ingrese un numero valido.")
               continue
           
            cant = int(cant)
            
            # .capitalize () = Convierte la primera letra de una cadena en Mayuscula
            # .strip() = Elimina espacios en blanco atras y adelante de la cadena
            
            for i in range(cant):
                espec = input("Ingrese el nombre de la especialidad que desea agregar: ").capitalize().strip()
                especialidades.append(espec)
                cupos.append(0)
            
        case '2':
            #Agreagar nuevos cupos a cada una de las especialidades existentes
            if not especialidades:
                print("No hay especialidades disponibles.")
                continue
            
            for i in range(len(especialidades)):
                cupo = input(f"Ingrese el cupo para la especialidad '{especialidades[i]}': ")
                
                if not cupo.isdigit():
                    print("Error. Debe ingresar un numero.")
                    break
                cupo = int(cupo)
                cupos [i] = cupo
            
        case '3':
            #Muestra todas las especialidades y el número de cupos disponibles para cada una
            if not especialidades:
                print("No hay especialidades disponibles.")
                continue
            
            for i in range(len(especialidades)):
                print(f"'{especialidades[i]}': {cupos[i]}.")
            
            
        case '4':
            # Verificar la disponibilidad de una especialidad específica
            if not especialidades:
                print("No hay especialidades disponibles.")
                continue
            
            #Validacion necesaria de .strip().capitalize() para que se compare lo mismo que ingrese el usuario con la lista
            
            especialidad = input("Ingrese una especialidad: ").strip().capitalize()
            
            if especialidad not in especialidades:
                print("Esta especialidad no existe un la lista.")
                
            #.index() = Busca el valor dentro de una lista y devuelve su posicion    
            
            else:
                ind = especialidades.index(especialidad)
                print(f"Cupos disponibles para {especialidad}: {cupos[ind]} cupos.")
            
            
            
        case '5':
            # Listar especialidades sin cupo
            if not especialidades:
                print("No hay especialidades disponibles.")
                continue
            
            for i in range(len(especialidades)):
                if (cupos[i] == 0):
                    print(especialidades[i])
                   
                       
        case '6':
            # Agregar especialidad: (Sumar una nueva especialidad a la lista)
            nombre_espec = input("Ingrese el nombre de la especialidad a agregar: ").strip().capitalize()
            especialidades.append(nombre_espec)
            
            cant_cupo = input(f"Ingrese la cantidad de cupos para {nombre_espec}: ")
            
            if not cant_cupo.isdigit():
                print("Error. Ingrese un numero valido.")
                continue
            cant_cupo = int(cant_cupo)
            cupos.append(cant_cupo)
            
        case '7':
            # Actualizar cupos (Reservar/Cancelar)
            if not especialidades:
                print("No hay especialidades disponibles.")
                continue
            especialidad = input("Ingrese una especialidad: ").strip().capitalize()
            
            if especialidad not in especialidades:
                print("Esta especialidad no existe un la lista.")
            else:
                ind = especialidades.index(especialidad)
                print(f"Cupos disponibles para {especialidad}: {cupos[ind]} cupos.")
                opc = input("Ingrese r para Reservar ó c para Cancelar un cupo: ").lower()
                
                match opc:
                    case 'r':
                        if (cupos[ind] == 0):
                            print("No hay cupos disponibles para reservar.")
                        else:
                            cupos[ind] -= 1
                            print("Reserva realizada.")
                    case 'c':
                        cupos[ind] += 1
                        print("Cancelacion realizada.")
                    case _:
                        print("Opcion Invalida.")
                
            
        case '8':
            # Mostrar Especialidades con sus cupos correspondientes (No muestra vacias)
            if not especialidades:
                print("No hay especialidades disponibles.")
                continue
            for i in range(len(especialidades)):
                if (cupos[i] != 0):
                    print(f"-> {especialidades[i]}")
            
            
        case '9':
            print("Gracias por usar el programa de la Clinica, vuelva pronto.")
            break
        case _:
            print("Opcion invalida. Vuelviendo al menu principal...")
            continue