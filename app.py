
# First Flask application
# Irdi Caushaj
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        return "Buy, World"
    return "Hello, World"

@app.route('/inf310c')
def inf310c():
    return "Microservices with the Flask Microframework using Python"
