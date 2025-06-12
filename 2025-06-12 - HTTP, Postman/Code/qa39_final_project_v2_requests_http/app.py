import random

from flask import Flask, request, jsonify, render_template
from models.models import Product
from services import product_service

app = Flask(__name__)


@app.route('/other/home')
def other_home():
    return render_template('/other_website/home.html')


@app.route('/other/next')
def other_next():
    return render_template('/other_website/nextpage.html')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/products', methods=['GET'])
def get_all():
    products = product_service.get_all_products()
    return jsonify([p.__dict__ for p in products])


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_one(product_id):
    try:
        product = product_service.get_product(product_id)
        if product:
            return jsonify(product.__dict__)
        return jsonify({"error": "Product not found"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/products', methods=['POST'])
def create():
    data = request.get_json()
    try:
        new_product = Product(
            product_id=0,
            name=data['name'],
            price=float(data['price']),
            image=data['image']
        )
        new_id = product_service.add_product(new_product)
        return jsonify({"message": "Product added", "id": new_id}), 201
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update(product_id):
    data = request.get_json()
    try:
        updated_product = Product(
            product_id=product_id,
            name=data['name'],
            price=float(data['price']),
            image=data['image']
        )
        success = product_service.update_product(updated_product)
        if success:
            return jsonify({"message": "Product updated"})
        return jsonify({"error": "Product not found"}), 404
    except (KeyError, ValueError) as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete(product_id):
    success = product_service.delete_product(product_id)
    if success:
        return jsonify({"message": "Product deleted"})
    return jsonify({"error": "Product not found"}), 404


@app.route('/api/rand', methods=['GET'])
def random_number():
    return str(random.randint(100, 201))


@app.route('/api/name', methods=['GET'])
def my_name():
    return 'Eldar'


@app.route('/api/numbers/<float:num1>/<float:num2>', methods=['GET'])
def add_numbers(num1, num2):
    result = num1 + num2
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
