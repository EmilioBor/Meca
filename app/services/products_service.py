# Simulamos DB en memoria
products = {
    "1": {"name": "Laptop", "price": 1000},
    "2": {"name": "Smartphone", "price": 500},
    "3": {"name": "Tablet", "price": 300}
}


def get_all_products():
    return products


def get_product_by_id(product_id):
    return products.get(product_id)


def create_product(data):
    new_id = str(len(products) + 1)
    products[new_id] = {
        "name": data["name"],
        "price": data["price"]
    }
    return {"message": "Producto creado", "product_id": new_id, "product": products[new_id]}


def update_product(product_id, data):
    if product_id in products:
        products[product_id] = {
            "name": data["name"],
            "price": data["price"]
        }
        return {"message": "Producto actualizado", "product": products[product_id]}
    return None


def delete_product(product_id):
    return products.pop(product_id, None)
