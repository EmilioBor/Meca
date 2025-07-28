from flask import Blueprint, request, jsonify
from app.services.products_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)

products_bp = Blueprint('products', __name__)


@products_bp.route('/', methods=['GET'])
def get_all():
    return jsonify(get_all_products()), 200


@products_bp.route('/<product_id>', methods=['GET'])
def get_one(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404


@products_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    return jsonify(create_product(data)), 201


@products_bp.route('/<product_id>', methods=['PUT'])
def update(product_id):
    data = request.get_json()
    updated = update_product(product_id, data)
    if updated:
        return jsonify(updated), 200
    return jsonify({"error": "Product not found"}), 404


@products_bp.route('/<product_id>', methods=['DELETE'])
def delete(product_id):
    deleted = delete_product(product_id)
    if deleted:
        return jsonify({"message": "Producto eliminado", "product": deleted}), 200
    return jsonify({"error": "Product not found"}), 404
