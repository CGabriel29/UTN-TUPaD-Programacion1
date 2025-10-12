# Función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

# Mostrar el resultado con dos decimales
print("Equivalente en Fahrenheit:", round(fahrenheit, 2))
