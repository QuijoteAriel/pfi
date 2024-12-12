import sqlite3

ruta_db = "pfi/inventario.db"

def db_crear_tabla_productos():
    try:
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()  # siempre igual
        cursor.execute(
            """ 
            CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            categoria TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
            )
            """
        )
        conexion.commit()
    except sqlite3.Error as e:
        print(f'Error al crear la tabla: {e}')
    finally:
        conexion.close()

if __name__ == "__main__":
    db_crear_tabla_productos()
    
# def db_agregar_producto(nombre, descripcion, categoria, cantidad, precio):
#         try:
#             conexion = sqlite3.connect(ruta_db)
#             cursor = conexion.cursor()  # siempre igual
#             # query = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)"
#             query = "INSERT INTO productos  VALUES (NULL, ?, ?, ?, ?, ?)"
#             placeholder = (nombre, descripcion, categoria, cantidad, precio)
#             cursor.execute(query, placeholder)
#             conexion.commit()
#         except Exception as error:
#             print(f"Error: {error}")
#         finally:
#             conexion.close()
