# Lista para almacenar las valoraciones y comentarios...
valoraciones = []

def main():
    while True:
        print("\nPor favor, elige una opción:")
        print("1. Introducir punto de valoración")
        print("2. Ver resultados")
        print("3. Salir")
        
        try:
            num = int(input("Introduce un número del 1 al 3: "))
            
            if num == 1:
                introducir_valoracion()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                print('Saliendo del programa...')
                break
            else:
                print('Por favor, introduce un número del 1 al 3.')
        except ValueError:
            print('Eso no es un número válido. Intenta de nuevo.')

def introducir_valoracion():
    while True:
        try:
            valoracion = int(input("¿Cuál es tu valoración del 1 al 5? "))
            if 1 <= valoracion <= 5:
                comentario = input("Deja un comentario: ")
                # Guardamos la valoración y el comentario
                valoraciones.append((valoracion, comentario))
                print(f'Valoración registrada: {valoracion}, Comentario: "{comentario}"')
                break
            else:
                print('Introduce un número entre 1 y 5, por favor.')
        except ValueError:
            print('Eso no es un número. Intenta nuevamente.')

def comprobar_resultados():
    if valoraciones:
        print("\nResultados de valoraciones:")
        for valoracion, comentario in valoraciones:
            print(f"Valoración: {valoracion}, Comentario: {comentario}")
    else:
        print("No hay valoraciones registradas aún.")

if __name__ == "__main__":
    main()
