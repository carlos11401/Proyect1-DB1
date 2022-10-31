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

if __name__ == '__main__':
    app.run()
    
