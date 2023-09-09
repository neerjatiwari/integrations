# app/routes.py

from flask import request, jsonify, url_for
from app import app, db
from app.models import Customer

@app.route('/api/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    customer_list = [{'id': customer.id, 'name': customer.name, 'email': customer.email} for customer in customers]
    return jsonify(customer_list)

@app.route('/api/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer = Customer(name=data['name'], email=data['email'])
    db.session.add(customer)
    db.session.commit()
    return jsonify({'message': 'Customer created successfully'}), 201

@app.route('/api/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify({'id': customer.id, 'name': customer.name, 'email': customer.email})

