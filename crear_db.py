import sqlite3

# Conectar (o crear si no existe)
conn = sqlite3.connect("compras.db")

# Crear cursor
cursor = conn.cursor()

# Crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS compras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        compra TEXT NOT NULL
    )
""")

# Confirmar y cerrar
conn.commit()
conn.close()

print("Base de datos y tabla creada correctamente.")
