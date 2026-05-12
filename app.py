from flask import Flask, jsonify, request

app = Flask(__name__)

bd_productos = [
    {"id": 1, "nombre": "Torta de Chocolate", "precio": 15000, "stock": 10},
    {"id": 2, "nombre": "Kuchen de Nuez", "precio": 12000, "stock": 5}
]

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "success", "message": "API Pastelería Operativa"}), 200

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    return jsonify({"productos": bd_productos}), 200

@app.route('/api/productos', methods=['POST'])
def crear_producto():
    datos = request.get_json()
    if not datos or 'nombre' not in datos or 'precio' not in datos:
        return jsonify({"error": "Faltan datos obligatorios (nombre, precio)"}), 400
    
    nuevo_id = max([p['id'] for p in bd_productos]) + 1 if bd_productos else 1
    nuevo_producto = {
        "id": nuevo_id,
        "nombre": datos['nombre'],
        "precio": datos['precio'],
        "stock": datos.get('stock', 0)
    }
    bd_productos.append(nuevo_producto)
    return jsonify({"mensaje": "Producto creado con éxito", "producto": nuevo_producto}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)