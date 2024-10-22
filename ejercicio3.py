from abc import ABC, abstractmethod


class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre  
        self._precio = precio

    
    @abstractmethod
    def calcular_precio_final(self):
        pass

    
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio



class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def calcular_precio_final(self):
      
        return self._precio * 0.9


class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def calcular_precio_final(self):
        
        return self._precio


class Zapatos(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def calcular_precio_final(self):
       
        return self._precio * 0.85



class CarritoDeCompras:
    def __init__(self):
        self._productos = []  

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.calcular_precio_final() 
        return total

    def mostrar_productos(self):
        for producto in self._productos:
            print(f"Producto: {producto.get_nombre()}, Precio Final: {producto.calcular_precio_final():.2f}")



class Tienda:
    def __init__(self):
        self.carrito = CarritoDeCompras()

    def mostrar_menu(self):
        print("Bienvenido a la Tienda de Ropa")
        print("1. Agregar Camisa")
        print("2. Agregar Pantalón")
        print("3. Agregar Zapatos")
        print("4. Ver Carrito")
        print("5. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nombre = input("Nombre de la camisa: ")
                precio = float(input("Precio: "))
                talla = input("Talla: ")
                camisa = Camisa(nombre, precio, talla)
                self.carrito.agregar_producto(camisa)
                print(f"{nombre} agregada al carrito.")

            elif opcion == "2":
                nombre = input("Nombre del pantalón: ")
                precio = float(input("Precio: "))
                talla = input("Talla: ")
                pantalon = Pantalon(nombre, precio, talla)
                self.carrito.agregar_producto(pantalon)
                print(f"{nombre} agregado al carrito.")

            elif opcion == "3":
                nombre = input("Nombre de los zapatos: ")
                precio = float(input("Precio: "))
                talla = input("Talla: ")
                zapatos = Zapatos(nombre, precio, talla)
                self.carrito.agregar_producto(zapatos)
                print(f"{nombre} agregados al carrito.")

            elif opcion == "4":
                print("Productos en el carrito:")
                self.carrito.mostrar_productos()
                total = self.carrito.calcular_total()
                print(f"Total a pagar: {total:.2f}")

            elif opcion == "5":
                print("Gracias por su compra!")
                break

            else:
                print("Opción no válida, intenta nuevamente.")



if __name__ == "__main__":
    tienda = Tienda()
    tienda.ejecutar()
