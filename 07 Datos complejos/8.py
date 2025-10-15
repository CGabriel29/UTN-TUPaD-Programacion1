# Diccionario inicial de productos y su stock
stock_productos = {
    "Arroz": 50,
    "Fideos": 30,
    "Aceite": 20
}

# Solicitar al usuario el nombre del producto
producto = input("Ingresá el nombre del producto que querés consultar o actualizar: ")

# Verificar si el producto ya existe en el diccionario
if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]} unidades")
    
    # Preguntar si desea agregar unidades
    agregar = input("¿Querés agregar unidades al stock? (sí/no): ").lower()
    if agregar == "sí":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
else:
    print(f"{producto} no está registrado.")
    
    # Preguntar si desea agregar el nuevo producto
    nuevo = input("¿Querés agregar este producto al inventario? (sí/no): ").lower()
    if nuevo == "sí":
        unidades = int(input("¿Cuántas unidades tiene?: "))
        stock_productos[producto] = unidades
        print(f"{producto} agregado con {unidades} unidades.")

# Mostrar el estado final del inventario
print("\nInventario actualizado:")
for nombre, cantidad in stock_productos.items():
    print(f"{nombre}: {cantidad} unidades")
