# Definir los vectores
nombres = []
precios = []
cantidades_vendidas = []

# Función para introducir un artículo nuevo
def introducir_articulo():
    nombre = input("Introduce el nombre del artículo: ")
    precio = float(input("Introduce el precio del artículo: "))
    nombres.append(nombre)
    precios.append(precio)
    cantidades_vendidas.append(0)

# Función para hacer una venta
def hacer_venta():
    nombre = input("Introduce el nombre del artículo: ")
    cantidad = int(input("Introduce la cantidad a vender: "))
    indice = nombres.index(nombre)
    cantidades_vendidas[indice] += cantidad

# Función para mostrar información
def mostrar_informacion():
    total = 0
    print("{:<20} {:<10} {:<10} {:<10}".format("Nombre", "Precio", "Cantidad", "Importe"))
    for i in range(len(nombres)):
        importe = precios[i] * cantidades_vendidas[i]
        total += importe
        print("{:<20} {:<10} {:<10} {:<10}".format(nombres[i], precios[i], cantidades_vendidas[i], importe))
    print("{:<20} {:<10} {:<10} {:<10}".format("Total", "", "", total))

# Función para borrar un artículo
def borrar_articulo():
    nombre = input("Introduce el nombre del artículo: ")
    indice = nombres.index(nombre)
    del nombres[indice]
    del precios[indice]
    del cantidades_vendidas[indice]

# Función para borrar todos los artículos
def borrar_todos_los_articulos():
    nombres.clear()
    precios.clear()
    cantidades_vendidas.clear()

# Función para mostrar el menú
def mostrar_menu():
    print("1. Introducir un artículo nuevo")
    print("2. Hacer una venta")
    print("3. Mostrar información")
    print("4. Borrar un artículo")
    print("5. Borrar todos los artículos")
    print("6. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = int(input("Introduce una opción: "))
    if opcion == 1:
        introducir_articulo()
    elif opcion == 2:
        hacer_venta()
    elif opcion == 3:
        mostrar_informacion()
    elif opcion == 4:
        borrar_articulo()
    elif opcion == 5:
        borrar_todos_los_articulos()
    elif opcion == 6:
        break
    else:
        print("Opción no válida")
