from flask import Flask, request, jsonify
import products_dao
import units_dao
from sql_connection import get_sql_conncetion

app = Flask(__name__)

connection = get_sql_conncetion()

@app.route('/getProducts', methods = ['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getUnits', methods = ['GET'])
def get_units():
    response = units_dao.get_units(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods = ['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods = ['POST'])
def insert_product():
    request_payload = request.form['data']
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server")
    app.run(port = 5000)