import json

from flask import Flask, request
from flask_restful import Resource, Api, reqparse


from encoder import concat


app = Flask(__name__)
api = Api(app)

class Root(Resource):
    def get(self):
        return {'version': 'v0.1.0'}

def ClipArgument(input):
    return input['url']

def OutputArgument(input):
    return {
        'type': input['type'],
        'location': input['location']
    }

class Concat(Resource):
    def post(self):
        json = request.json

        head_file = json['head']['url']
        tail_file = json['tail']['url']
        output_type = json['output']['type']
        output_location = json['output']['location']
        webhook = json['webhook_url']
        authorization = json['authorization']

        #authorize(head_file, tail_file, webhook, authorization)
        concat(head_file, tail_file, output_location)
        # trigger_webhooks()
        return json, 200

api.add_resource(Root, '/')
api.add_resource(Concat, '/concat/')

if __name__ == '__main__':
    app.run(debug=True, port=9009)