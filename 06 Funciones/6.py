# Función que imprime la tabla de multiplicar del número recibido
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

# Programa principal
numero_ingresado = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero_ingresado)
