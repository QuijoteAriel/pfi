import sqlite3

#ruta_db = "~/inventario.db"

def db_crear_tabla_productos():
    conexion = sqlite3.connect('inventario.db')
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
    conexion.close()


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
