
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
            buscar_producto()
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


    if not mostrar:
        print('No hay productos en el inventario')
    else:
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
    except sql.Error as e:
        print(f"Error al actualizar la cantidad: {e}")
    finally:
        conexion.commit()
        conexion.close()

def eliminar_producto():
    conexion = sql.connect('inventario.db')
    cursor = conexion.cursor()
    id_producto = input('Que ID quieres eliminar ? ')
    cursor.execute("DELETE FROM productos WHERE id=? ", (id_producto))

    if cursor.rowcount > 0:
        print(f'Id {id_producto} del producto fue eliminado correctamente')
    else:
        print('El Id no encontrado / no existe')
    
    conexion.commit()
    conexion.close()

def buscar_producto():
    """Busca un producto en la base de datos por nombre, categoría o ID."""

    def buscar(campo, valor):
        """Función auxiliar para realizar la consulta a la base de datos."""
        conn = sql.connect('inventario.db')
        cursor = conn.cursor()
        instruccion = f"SELECT * FROM productos WHERE {campo} LIKE ?"
        cursor.execute(instruccion, (f"%{valor}%",))
        resultados = cursor.fetchall()
        conn.close()
        return resultados

    while True:
        print("Desea buscar un producto por:")
        print("1. Nombre")
        print("2. Categoría")
        print("3. ID")
        opcion = input("Seleccione una opción (o presione Enter para salir): ")

        if not opcion:
            break

        if opcion in ('1', '2', '3'):
            if opcion == '1':
                campo = 'nombre'
            elif opcion == '2':
                campo = 'categoria'
            else:
                campo = 'id'

            valor = input(f"Ingrese el {campo} del producto: ")
            resultados = buscar(campo, valor)

            if not resultados:
                print(f"No se encontraron productos con el {campo} '{valor}'.")
            else:
                print("Productos encontrados:")
                for producto in resultados:
                    id, nombre, descripcion, precio, cantidad, categoria = producto
                    print(f"ID: {id}")
                    print(f"Nombre: {nombre}")
                    print(f"Descripcion: {descripcion}")
                    print(f"Precio: {precio}")
                    print(f"Cantidad: {cantidad}")
                    print(f"Categoria: {categoria}")
        else:
            print("Opción inválida.")

def bajo_stock():
    pass


        
# Ejecución de la función main() - (NO ELIMINAR)
if __name__ == "__main__":
    main()
