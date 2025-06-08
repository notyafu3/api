from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'compras.db'

# Función para conectar con la base de datos
def conectar_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# 👉 Crear compra
@app.route('/compras', methods=['POST'])
def agregar_compra():
    data = request.get_json()
    compra = data.get('compra')

    if not compra:
        return jsonify({"error": "Campo 'compra' es obligatorio"}), 400

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO compras (compra) VALUES (?)", (compra,))
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "Compra agregada correctamente"}), 201

# 👉 Leer todas las compras
@app.route('/compras', methods=['GET'])
def obtener_compras():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compras")
    compras = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(compras)

# 👉 Actualizar una compra
@app.route('/compras/<int:id>', methods=['PUT'])
def actualizar_compra(id):
    data = request.get_json()
    nueva_compra = data.get('compra')

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE compras SET compra = ? WHERE id = ?", (nueva_compra, id))
    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Compra actualizada correctamente"})

# 👉 Borrar una compra
@app.route('/compras/<int:id>', methods=['DELETE'])
def eliminar_compra(id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM compras WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Compra eliminada correctamente"})

# 👉 Ejecutar app
if __name__ == '__main__':
    app.run(debug=True)
