from flask import Flask, jsonify, render_template, request
from db import DataBase

app = Flask(__name__)
db = DataBase()

@app.route('/', methods=['POST'])
def init():
    return "Hello World!!!"

@app.route('/1consult', methods=['POST'])
def customerWithMorePurchases():
    customer = db.get_customerWithMorePurchases()
    return jsonify(customer)

@app.route('/2consult', methods=['POST'])
def max_min_amounts():
    products = db.get_moreAndLessPurchasedProducts()
    return jsonify(products)

@app.route('/3consult', methods=['POST'])
def sellerWithMoreSales():
    seller = db.get_sellerWithMoreSales()
    return jsonify(seller)

if __name__ == '__main__':
    app.run()
    
