productos = []

def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ")
    
    while True:
        try:
            precio_producto = float(input("Ingrese el precio del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")
    
    while True:
        try:
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")

    productos.append({"nombre": nombre, "precio": precio_producto, "cantidad": cantidad_producto})
    print(f"Producto '{nombre}' añadido con un precio de '{precio_producto}' y cantidad '{cantidad_producto}'.")

def ver_productos():
    if not productos:
        print("No hay productos disponibles.")
    else:
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")

def actualizar_producto():
    ver_productos()
    if productos:
        while True:
            try:
                nuevo_producto = int(input("Seleccione el número del producto que desea cambiar: ")) - 1
                if 0 <= nuevo_producto < len(productos):
                    break
                else:
                    print("Número de producto no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        nom_producto = input("Ingrese el nombre del nuevo producto: ")
        
        while True:
            try:
                precio_nuevo = float(input("Ingrese el nuevo precio del producto: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el precio.")

        while True:
            try:
                cantidad_nueva = int(input("Ingrese la nueva cantidad del producto: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido para la cantidad.")

        productos[nuevo_producto] = {'nombre': nom_producto, 'precio': precio_nuevo, 'cantidad': cantidad_nueva}
        print("Producto actualizado con éxito!")

def eliminar_producto():
    ver_productos()
    if productos:
        while True:
            try:
                eliminar_producto = int(input("Ingrese el número del producto que desea eliminar: ")) - 1
                if 0 <= eliminar_producto < len(productos):
                    break
                else:
                    print("Número de producto no válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        eliminando = productos.pop(eliminar_producto)
        print(f"Producto '{eliminando['nombre']}' eliminado con éxito.")

def guardar_datos():
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")
    print("Datos guardados correctamente.")

def cargar_datos():
    global productos
    try:
        with open('productos.txt', 'r') as file:
            productos = []
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                productos.append({'nombre': nombre, 'precio': float(precio), 'cantidad': int(cantidad)})
        print("Datos cargados.")
    except FileNotFoundError:
        print("No hay datos para cargar.")

def menu():
    cargar_datos()  # Cargar datos al iniciar
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()
