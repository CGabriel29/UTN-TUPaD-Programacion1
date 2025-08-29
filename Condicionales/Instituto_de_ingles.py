#Solicitar fecha
dia_texto= input ("Ingrese el dia de la semana: ") .strip().lower()
dia_num = int (input ("Numero de dia (1-31): "))
mes_num= int (input ("Numero de mes (1-12): "))

#Mapear el dia textual a numero

if dia_texto == "lunes":
    dia_semana = 1
elif dia_texto == "martes":
    dia_semana = 2
elif dia_texto == "miercoles":
    dia_semana = 3
elif dia_texto == "jueves":
    dia_semana = 4
elif dia_texto == "viernes":
    dia_semana = 5
else:
    print ("Se produjo un error: dia de la semana invalido.")
    exit()
# Validar fecha

if dia_num < 1 or dia_num > 31 or mes_num < 1 or mes_num > 12:
    print ("Se produjo un error en la fecha.")
    exit()

# Procesar segun el dia

if dia_semana == 1:
    print ("Nivel: inicial")
    examen = int (input("Se tomaron examenes? (1=si, 0=no): "))
    if examen == 1:
        aprobados = int (input ("Cantidad de aprobados: "))
        desaprobados = int (input("Cantidad de desaprobados: "))
        total = aprobados + desaprobados
        if total > 0:
                 porcentaje = (aprobados/total)*100
                 print(f"Porcetaje de aprobados: {porcentaje: .2f}%")
        else: 
                 print("No se ingresaron alumnos.")

elif dia_semana == 2:
    print("Nivel: Intermedio")
    examen = int (input("Se tomaron examenes? (1=si, 0=no): "))
    if examen == 1:
        aprobados = int (input ("Cantidad de aprobados: "))
        desaprobados = int (input("Cantidad de desaprobados: "))
        total = aprobados + desaprobados
        if total > 0:
                 porcentaje = (aprobados/total)*100
                 print(f"Porcetaje de aprobados: {porcentaje: .2f}%")
        else: 
                 print("No se ingresaron alumnos.")

elif dia_semana == 3:
    print("Nivel: Avanzado")
    examen = int (input("Se tomaron examenes? (1=si, 0=no): "))
    if examen == 1:
        aprobados = int (input ("Cantidad de aprobados: "))
        desaprobados = int (input("Cantidad de desaprobados: "))
        total = aprobados + desaprobados
        if total > 0:
                 porcentaje = (aprobados/total)*100
                 print(f"Porcetaje de aprobados: {porcentaje: .2f}%")
        else: 
                 print("No se ingresaron alumnos.") 

elif dia_semana == 4:
    print("Nivel: Practica hablada")
    asistencia = float (input("Porcentaje de asistencia: "))
    if asistencia > 50:
        print("Asistio la mayoria.")
    else:
        print("No asistio la mayoria")

elif dia_semana == 5:
    print("Nivel: Ingles para viajeros")
    if dia_num == 1 and (mes_num == 1 or mes_num == 7):
       print("Comienzo de nuevo ciclo.")
       alumnos = int (input("Cantidad de alumnos: "))
       arancel = float (input("Arancel para alumno ($): "))
       ingreso = alumnos * arancel
       print(f"Ingreso total: ${ingreso:.2f}")