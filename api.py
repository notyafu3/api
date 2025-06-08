from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # 🔥 Habilita CORS para todas las rutas y orígenes

# Funciones auxiliares para DB
def conectar():
    return sqlite3.connect('compras.db')

@app.route('/compras', methods=['GET'])
def obtener_compras():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, compra FROM compras")
    datos = cur.fetchall()
    con.close()
    return jsonify([{'id': id, 'compra': compra} for id, compra in datos])

@app.route('/compras', methods=['POST'])
def agregar_compra():
    data = request.get_json()
    compra = data.get('compra')
    if not compra:
        return jsonify({'error': 'Campo "compra" requerido'}), 400
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO compras (compra) VALUES (?)", (compra,))
    con.commit()
    con.close()
    return jsonify({'mensaje': 'Compra agregada correctamente'}), 201

@app.route('/compras/<int:id>', methods=['DELETE'])
def eliminar_compra(id):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM compras WHERE id = ?", (id,))
    con.commit()
    con.close()
    return jsonify({'mensaje': 'Compra eliminada correctamente'}), 200

# Ejecutar app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
