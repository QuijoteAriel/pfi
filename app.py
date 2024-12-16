
from funcion_db import *
# from colorama

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
    conexion = sql.connect('inventario.db')
    cursor = conexion.cursor()

    try:
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

        # Ejecutar la consulta con parámetros para prevenir inyección SQL
        cursor.execute("UPDATE productos SET cantidad=? WHERE id=?", (nueva_cantidad, id_producto))

        # Comprobar si se actualizaron filas
        filas_afectadas = cursor.rowcount
        if filas_afectadas > 0:
            print(f"Se actualizó la cantidad del producto con ID {id_producto}")
        else:
            print(f"No se encontró ningún producto con ID {id_producto}")

    except ValueError:
        print("Error: Debe ingresar un ID y una cantidad válidos (números enteros)")
    except sqlite3.Error as e:
        print(f"Error al actualizar la cantidad: {e}")
    finally:
        conexion.commit()
        conexion.close()

def eliminar_producto():
    conexion = sql.connect('inventario.db')
    cursor = conexion.cursor()
    try:
        id_producto = input('Que producto/ ID quieres eliminar ? ')
        cursor.execute("DELETE productos SET ID=? WHERE id=?", id_producto)

        print(f'Id {id_producto}eliminado correctamente')
    except:
        print('El Id no encontrado / no existe')
    finally:
        conexion.commit()
        conexion.close()

# Ejecución de la función main() - (NO ELIMINAR)
if __name__ == "__main__":
    main()
