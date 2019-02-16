from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Item(Resource):
    def get(self):
        return {'action': "GET"}
    def post(self):
        return {'action': "POST"}
    def put(self):
        return {'action': "PUT"}
    def delete(self):
        return {'action': "DELETE"}


api.add_resource(Item, '/item')