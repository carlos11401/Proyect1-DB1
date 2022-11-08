from flask import Flask, jsonify
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

@app.route('/4consult', methods=['POST'])
def contryWithMoreAndLessSales():
    seller = db.get_contryWithMoreAndLessSales()
    return jsonify(seller)

@app.route('/5consult', methods=['POST'])
def topContriesWithMorePurchases():
    seller = db.get_topContriesWithMorePurchases()
    return jsonify(seller)

@app.route('/6consult', methods=['POST'])
def categoryMoreAndLessAmounts():
    seller = db.get_categoryMoreAndLessAmounts()
    return jsonify(seller)

if __name__ == '__main__':
    app.run()