# Función que realiza las operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

# Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Llamada a la función
suma, resta, multiplicacion, division = operaciones_basicas(a, b)

# Mostrar resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
