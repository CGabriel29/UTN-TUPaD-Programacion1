# Función que calcula el índice de masa corporal
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

# Mostrar el resultado con dos decimales
print("Su índice de masa corporal (IMC) es:", round(imc, 2))
