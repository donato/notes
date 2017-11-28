from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Root(Resource):
    def get(self):
        return {'version': 'v0.1.0'}

class Concat(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('head')
        parser.add_argument('tail')
        parser.add_argument('output')
        parser.add_argument('authorization')
        parser.add_argument('webhooks')

        args = parser.parse_args()
        return args, 201

api.add_resource(Root, '/')
api.add_resource(Concat, '/concat/')

if __name__ == '__main__':
    app.run(debug=True, port=9009)