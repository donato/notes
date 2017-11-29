import json

from flask import Flask, request
from flask_restful import Resource, Api, reqparse


from encoder import concat
from cloud import get_file_public_url, put_file_to_s3


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

        head_file = json['head']['path']
        head_file_location = json['head']['location']
        tail_file = json['tail']['path']
        tail_file_location = json['tail']['location']
        output_type = json['output']['type']
        output_location = json['output']['location']
        webhook = json['webhook_url']
        authorization = json['authorization']

        if head_file_location == 'web':
            local_head_file = get_file_public_url(head_file)
        elif head_file_location == 'local':
            local_head_file = head_file
        else:
            raise 'Bad file location'
        if tail_file_location == 'web':
            local_tail_file = get_file_public_url(tail_file)
        elif tail_file_location == 'local':
            local_tail_file = tail_file
        else:
            raise 'Bad file location'

        #authorize(head_file, tail_file, webhook, authorization)
        tmp_file = concat(local_head_file, local_tail_file)

        s3_url = put_file_to_s3(tmp_file)
        print(s3_url)

        # trigger_webhooks()
        return {
            "request": json,
            "output": s3_url
        }, 200

api.add_resource(Root, '/')
api.add_resource(Concat, '/concat/')

if __name__ == '__main__':
    app.run(debug=True, port=9009)