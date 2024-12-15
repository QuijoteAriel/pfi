
from funcion_db import *
# from colorama

productos = []

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
       
# Funcion principal, la funcion siempre vuelve a ejecutrase cada vez que se realice una accion valida en el programa        
        
        try:
            opcion = int(input('Elija una opción: '))
        except ValueError:
            print("Opción inválida. Debe ingresar un número entero.")
            continue  # Continuamos el bucle si no es un número válido

        if opcion == 1:
            print('Agregar Producto')
            registrar_producto()
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


# Funcion registrar  genera un dicccionario a partir de inputs con los datos que se piden    
def registrar_producto():
  
    nombre = input('Ingrese el nombre del producto: ')
    descripcion = input('Ingrese la descrición del producto: ')
    cantidad = int(input('Ingrese la cantida: '))
    precio = float(input('Ingrese precio: '))
    categoria = input('Ingrese la categoria: ')

    conexion = sql.connect('inventario.db')
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO productos(nombre , descripcion, cantidad, precio,  categoria) VALUES(?, ? , ?, ?, ? )"
    cursor.execute(instruccion,(nombre, descripcion,cantidad,  precio, categoria))

    print(f" Producto '{nombre}' , agregado " )    
    conexion.commit()
    conexion.close()


    
 # Funcion mostrar, muestra todo lo que esta en el inventario    
def mostrar_productos():
    conexion = sql.connect('inventario.db')
    cursor = conexion.cursor()
    instruccion = f" SELECT * FROM productos"
    cursor.execute(instruccion)
    mostrar = cursor.fetchall()
    conexion.commit()
    conexion.close()

    print('Inventario actual: ')
    print('''
        
       ###################
         ABASTO DON JOSE
       ###################
        ''')

    for i in mostrar:
        id, nombre, descripcion, cantidad, precio, categoria = i
        print(f'''ID: {id}
        Nombre: {nombre}
        Descripcion: {descripcion}
        Cantidad: {cantidad}
        Precio: {precio}
        Categoria: {categoria}        
        ''')

# Funcion actualziar , actualiza la canditad del producto seleccionandolo por su ID 
def actualizar_cantidad():
    if not productos:
        print('No hay productos')
    else:
        clave_prod = input('Que clave/producto deseas cambiar la cantidad? : ')
        if clave_prod in productos:
            actualizar_can = int(input('Que cantidad deseas actualziar? : '))
            productos[clave_prod] = actualizar_can
            print('Cantidad actualizada correctamente')
        else:
            print('La clave seleccionada no existe')

def eliminar_producto(productos):
    borrar = input("¿Qué producto desea eliminar? : ")


    # Buscamos el índice del diccionario que queremos eliminar
    for i, producto in enumerate(productos):
        if producto["nombre"] == borrar:
            # Eliminamos el elemento por su índice
            del productos[i]
            print(f"El producto {borrar} se ha eliminado.")
            return  # Salimos de la función una vez que encontramos y eliminamos el producto

    # Si no encontramos el producto, mostramos un mensaje de error
    print(f"El producto {borrar} no se encontró.")
  


# Ejecución de la función main() - (NO ELIMINAR)
if __name__ == "__main__":
    main()
