from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada en memoria
products = {
    "1": {"name": "Laptop", "price": 1000},
    "2": {"name": "Smartphone", "price": 500},
    "3": {"name": "Tablet", "price": 300}
}


@app.route("/")
def home():
    return "¡Bienvenido a la API de productos!", 200


# Buscar todos los productos
@app.route("/products", methods=["GET"])
def get_all_products():
    return jsonify(products), 200


# Buscar un producto por ID
@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    product = products.get(product_id)
    query = request.args.get('query')

    if product:
        if query:
            return jsonify({
                "message": "Query received",
                "product_id": product_id,
                "query": query,
                "product": product
            }), 200
        else:
            return jsonify(product), 200
    else:
        return jsonify({"error": "Product not found"}), 404


# Crear producto
@app.route("/products", methods=["POST"])
def create_product():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_id = str(len(products) + 1)
    products[new_id] = {
        "name": data["name"],
        "price": data["price"]
    }

    return jsonify({
        "message": "Producto creado",
        "product_id": new_id,
        "product": products[new_id]
    }), 201


# Editar producto existente
@app.route("/products/<product_id>", methods=["PUT"])
def update_product(product_id):
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Invalid input"}), 400

    products[product_id] = {
        "name": data["name"],
        "price": data["price"]
    }

    return jsonify({
        "message": "Producto actualizado",
        "product_id": product_id,
        "product": products[product_id]
    }), 200


# Eliminar producto
@app.route("/products/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    deleted = products.pop(product_id)
    return jsonify({
        "message": "Producto eliminado",
        "product_id": product_id,
        "deleted_product": deleted
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
