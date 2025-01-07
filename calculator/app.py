from flask import Flask, request, jsonify
import math
import requests

app = Flask(__name__)

# Basic Arithmetic
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    x = data.get('x')
    y = data.get('y')

    if operation == 'add':
        return jsonify(result=x + y)
    elif operation == 'subtract':
        return jsonify(result=x - y)
    elif operation == 'multiply':
        return jsonify(result=x * y)
    elif operation == 'divide':
        if y == 0:
            return jsonify(error="Division by zero"), 400
        return jsonify(result=x / y)
    # Add more operations as needed

# Currency Conversion
@app.route('/convert_currency', methods=['GET'])
def convert_currency():
    amount = request.args.get('amount', type=float)
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    # Use a currency conversion API to get the rates
    # Example: response = requests.get(f'API_URL')
    # Implement conversion logic here
    return jsonify(converted_amount=amount)  # Placeholder

if __name__ == '__main__':
    app.run(debug=True)
