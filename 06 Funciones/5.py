# Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos_ingresados = float(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos_ingresados)

print("Equivalente en horas:", horas)
