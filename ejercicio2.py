productos = []

def añadir_producto():
    nombre = str(input("Ingrese el nombre del producto:"))
    precio_producto = float(input("Ingrese el precio del producto:"))
    
    productos.append({"nombre":nombre, "precio_producto":precio_producto})
    print(f"Producto '{nombre}' añadido con un precio de '{precio_producto}'")
    pass

def ver_productos():
    if not productos:
        print("No hay productos dispoibles")
    else:
        for i, producto in enumerate(productos, start = 1):
            print(f"{i}. {producto['nombre']} - Precio: {producto['precio_producto']}")
    pass

def actualizar_producto():
    ver_productos()
    if productos:
        nuevo_producto = int(input("Seleccione el numero del producto que desea cambiar:"))
        if 0 <= nuevo_producto < len(productos):
            nom_producto = str(input("Ingrese el nombre del nuevo producto:"))
            precio_nuevo = float(input("Ingrese el nuevo precio del producto:"))
            productos[nuevo_producto] = {'nombre': nom_producto, "precio":precio_nuevo}
            print("Producto actualizado con exito!")
        else:
            print("El producto no se pudo actualizar :(")
    pass

def eliminar_producto():
    ver_productos()
    if productos:
        eliminar_producto = int(input("Ingrese el numero del producto que desea eliminar:"))
        if 0 <= eliminar_producto < len(productos):
            eliminando = productos.pop(eliminar_producto)
            print(f"Producto '{eliminando['nombre']}' eliminado con éxito")
        else:
            print("El producto no se pudo eliminar :(")
    pass

def guardar_datos():
    with open("productos.txt","w") as file:
        for producto in productos:
            file.write(f"{producto["nombre"]}, {producto["precio"]}")
        print("Datos guardados correctamente")
    pass

def cargar_datos():
    global productos
    try:
        with open('productos.txt', 'r') as file:
            productos = []
            for line in file:
                nombre, precio = line.strip().split(',')
                productos.append({'nombre': nombre, 'precio': float(precio)})
        print("Datos cargados.")
    except FileNotFoundError:
        print("No hay datos para cargar.")

    pass

def menu():
    while True:
        print("1: Añadir producto")
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