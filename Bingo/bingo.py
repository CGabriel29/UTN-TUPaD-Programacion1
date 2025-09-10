import random

# 1. Generar cartón 5x5 con números únicos entre 1 y 50
numeros = random.sample(range(1, 51), 25)
carton = []
indice = 0
while indice < 25:
    fila = []
    for i in range(5):
        fila.append(numeros[indice])
        indice += 1
    carton.append(fila)

# 2. Mostrar el cartón inicial
print("Cartón inicial:")
for fila in carton:
    print(" ".join(f"{num:2}" for num in fila))
print()

# 3. Sorteo de números
numeros_sorteados = []

while True:
    numero = random.randint(1, 50)
    if numero in numeros_sorteados:
        continue
    numeros_sorteados.append(numero)
    print(f"Número sorteado: {numero}")

    encontrado = False
    for i in range(5):
        for j in range(5):
            if carton[i][j] == numero:
                carton[i][j] = 0
                encontrado = True

    if encontrado:
        print("¡Número encontrado y marcado!")
    else:
        print("No aparece en el cartón.")

    # 4. Mostrar el cartón actualizado
    print("Cartón actualizado:")
    for fila in carton:
        print(" ".join(f"{num:2}" for num in fila))
    print()

    # 5. Verificar si hay línea
    for fila in carton:
        ceros_en_fila = 0
        for num in fila:
            if num == 0:
                ceros_en_fila += 1
        if ceros_en_fila == 5:
            print("¡Línea!")

    # 6. Verificar si todo el cartón está en ceros
    ceros_totales = 0
    for i in range(5):
        for j in range(5):
            if carton[i][j] == 0:
                ceros_totales += 1

    if ceros_totales == 25:
        print("¡Bingo! Todos los números fueron marcados.")
        break
