
# Nombre del archivo
archivo = "productos.txt"

# 1. Crear archivo inicial si no existe
with open(archivo, "w") as f:
        f.write("Lapicera,120.5,30\n")
        f.write("Cuaderno,350.0,15\n")
        f.write("Goma,50.0,40\n")

# 2. Leer y mostrar productos
productos = []
with open(archivo, "r") as f:
    for linea in f:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)
        print(f"Producto: {nombre}\n Precio: ${precio}\n Cantidad: {cantidad}\n")

# 3. Agregar producto desde teclado

nombre = input("Ingrese el nombre del nuevo producto: ")

# Validar precio (debe ser número decimal)
precio_valido = False
while not precio_valido:
    precio_input = input("Ingrese el precio del producto: ")
    if precio_input.replace(".", "", 1).isdigit():
        precio_valido = True
    else:
        print("Error. El precio debe ser un número decimal. Intente nuevamente.")

# Validar cantidad (debe ser número entero)
cantidad_valida = False
while not cantidad_valida:
    cantidad_input = input("Ingrese la cantidad del producto: ")
    if cantidad_input.isdigit():
        cantidad_valida = True
    else:
        print("Error. La cantidad debe ser un número entero. Intente nuevamente.")

# Agregar al archivo sin borrar contenido
with open(archivo, "a") as arch:
    arch.write(f"{nombre},{precio_input},{cantidad_input}\n")

# También agregar el nuevo producto a la lista en memoria
productos.append({
    "nombre": nombre,
    "precio": float(precio_input),
    "cantidad": int(cantidad_input)
})

print("Producto agregado correctamente.")

# 4. Buscar producto por nombre
buscar = input("Ingresá el nombre de un producto para buscar: ")
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"\nProducto encontrado:\n Nombre: {p['nombre']}\n Precio: ${p['precio']}\n Cantidad: {p['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado.")

# 5. Guardar productos actualizados
with open(archivo, "w") as f:
    for p in productos:
        f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo actualizado correctamente.")
