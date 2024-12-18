import sqlite3 as sql

def create_data_base():
    conexion = sql.connect('inventario.db')
    conexion.commit()
    conexion.close()
    
def db_crear_tabla_productos():
    conexion = sql.connect('inventario.db') #creamos la base de datos
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

if __name__ == "__main__":
    create_data_base()
    db_crear_tabla_productos()
