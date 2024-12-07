productos = []
codigo_prod = 1
def main():
    while True:
        print('''
        
       ###################
         ABASTO DON JOSE
       ###################
        
     Elija una opción:

    1. Agregar Producto
    2. Mostrar Producto
    3. Actualizar Cantidad de Producto
    4. Eliminar Producto
    5. Buscar Producto
    6. Reporte de Bajo Stock
    7. Salir
        ''')
       
        try:
            opcion = int(input('Elija una opción: '))
        except ValueError:
            print("Opción inválida. Debe ingresar un número entero.")
            continue  # Continuamos el bucle si no es un número válido

        if opcion == 1:
            registrar_producto()
            print('Agregar Producto')
        elif opcion == 2:
            print('Mostrar Producto')
            mostrar_productos()
        elif opcion == 3:
            print("Actualizar cantidad de producto")
            actualizar_cantidad()
        elif opcion == 4:
            print("Eliminar producto")
            eliminar_producto()
        elif opcion == 5:
            print("Buscar producto")
            # Aquí podrías añadir código para buscar productos
        elif opcion == 6:
            print("Reporte de bajo stock")
            # Aquí podrías añadir código para reporte de bajo stock
        elif opcion == 7:
            print("Saliendo del sistema...")
            break  # Salir del bucle y terminar el programa
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            continue


def registrar_producto():
  
    nombre = input('Ingrese el nombre del producto: ')
    descripcion = input('Ingrese la descrición del producto: ')
    cantidad = int(input('Ingrese la cantida: '))
    precio = float(input('Ingrese precio: '))
    categoria = input('Ingrese la categoria: ')

    nuevo_producto = {
        'nombre': nombre,
        'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio,
        'categoria': categoria
        }
    productos.append(nuevo_producto)
    print('Producto registrado ', productos)
    
    
def mostrar_productos():
    if not productos:
        print('No hay productos')
    else:
        print("Lista de productos:")
        for i, producto in enumerate(productos, start=1):  # Enumeramos para mostrar el número de producto
            print(f"Producto {i}: nombre: {producto['nombre']}, descripcion: {producto['descripcion']}, cantidad: {producto['cantidad']} , precio: {producto['precio']}, categoria: {producto['categoria']}")        

def actualizar_cantidad():
    if not productos:
        print('No hay productos')
    elif clave_prod in productos:
        clave_prod = input('Que clave/producto deseas cambiar la cantidad ? : ')
        actualizar_can = input('Que cantidad deseas actualziar? : ')
        productos[clave_prod:actualizar_can]
        print('Cantidad actualizada correctamente')
    else:
        print('La clave seleccionada no existe ')

def eliminar_producto():
    pass

# Ejecución de la función main() - (NO ELIMINAR)
if __name__ == "__main__":
    main()
