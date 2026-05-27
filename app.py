from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
# Inicializamos Swagger para la documentación gráfica
swagger = Swagger(app)

# Base de datos simulada en memoria
productos = [
    {"id": 1, "nombre": "Torta de Chocolate", "precio": 15000},
    {"id": 2, "nombre": "Pie de Limón", "precio": 12000}
]

@app.route('/health', methods=['GET'])
def health_check():
    """
    Verifica el estado de la API
    ---
    responses:
      200:
        description: La API está funcionando correctamente
    """
    return jsonify({"status": "ok"}), 200

@app.route('/productos', methods=['GET'])
def get_productos():
    """
    Obtiene el menú completo de la pastelería
    ---
    responses:
      200:
        description: Lista de productos devuelta exitosamente
    """
    return jsonify(productos), 200

@app.route('/productos', methods=['POST'])
def create_producto():
    """
    Agrega un nuevo pastel al menú
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
              example: "Cheesecake de Frambuesa"
            precio:
              type: integer
              example: 18000
    responses:
      201:
        description: Producto creado exitosamente
      400:
        description: Bad Request (Faltan datos o formato incorrecto)
    """
    data = request.get_json()
    
    # Manejo de Errores: Validamos que envíen datos
    if not data or 'nombre' not in data or 'precio' not in data:
        return jsonify({"error": "Faltan datos requeridos (nombre, precio)"}), 400
    
    # Manejo de Errores: Validamos que el precio sea un número
    if not isinstance(data['precio'], (int, float)):
        return jsonify({"error": "El precio debe ser un número válido"}), 400

    nuevo_id = max([p['id'] for p in productos], default=0) + 1
    nuevo_producto = {
        "id": nuevo_id,
        "nombre": data['nombre'],
        "precio": data['precio']
    }
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

@app.route('/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    """
    Actualiza el precio o nombre de un pastel existente
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del producto a actualizar
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
            precio:
              type: integer
    responses:
      200:
        description: Producto actualizado
      400:
        description: Datos inválidos
      404:
        description: Producto no encontrado
    """
    # Buscamos si el producto existe
    producto = next((p for p in productos if p['id'] == id), None)
    
    # Manejo de Errores: Si no existe, devolvemos 404 Not Found
    if not producto:
        return jsonify({"error": f"El producto con ID {id} no existe"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron datos para actualizar"}), 400

    if 'nombre' in data:
        producto['nombre'] = data['nombre']
    if 'precio' in data:
        if not isinstance(data['precio'], (int, float)):
            return jsonify({"error": "El precio debe ser un número"}), 400
        producto['precio'] = data['precio']

    return jsonify(producto), 200

@app.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    """
    Elimina un pastel del menú
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del producto a eliminar
    responses:
      200:
        description: Producto eliminado
      404:
        description: Producto no encontrado
    """
    global productos
    producto = next((p for p in productos if p['id'] == id), None)
    
    # Manejo de Errores: 404 Not Found
    if not producto:
        return jsonify({"error": f"El producto con ID {id} no existe"}), 404

    productos = [p for p in productos if p['id'] != id]
    return jsonify({"mensaje": "Producto eliminado exitosamente"}), 200

if __name__ == '__main__':
    # Apagamos el debug o lo controlamos por entorno para producción
    app.run(debug=False, host='127.0.0.1', port=5000)