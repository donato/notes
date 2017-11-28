import json

from flask import Flask
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
    return input

class Concat(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('head', type=ClipArgument)
        parser.add_argument('tail', type=ClipArgument)
        parser.add_argument('output', type=OutputArgument)
        parser.add_argument('authorization')
        parser.add_argument('webhooks')
        args = parser.parse_args()

        head_file = args['head']
        tail_file = args['tail']
        output_type = args['output']['type']
        output_location = args['output']['location']
        webhook = args['webhooks']['url']
        authorization = args['authorization']

        # authorize(head_file, tail_file, webhook, authorization)
        concat(head_file, tail_file, output_location)
        # trigger_webhooks()
        """

        """
        return args, 200

api.add_resource(Root, '/')
api.add_resource(Concat, '/concat/')

if __name__ == '__main__':
    app.run(debug=True, port=9009)