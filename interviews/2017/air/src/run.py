from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from cloud import get_file_public_url, put_file_to_s3
from config import cfg
from encoder import concat


app = Flask(__name__)
api = Api(app)

class Root(Resource):
    def get(self):
        return {'version': 'v0.1.0'}

class Concat(Resource):
    def post(self):
        json = request.json

        head_file = json['head']['path']
        head_file_location = json['head']['location']
        tail_file = json['tail']['path']
        tail_file_location = json['tail']['location']
        output_type = json['output']['type']
        authorization = json['authorization']

        if authorization != cfg["AUTHORIZATION_KEY"]:
            return 401

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

        tmp_file = concat(local_head_file, local_tail_file)

        if output_type == 'web':
            output_file = put_file_to_s3(tmp_file)
        else:
            output_file = tmp_file

        print(output_file)

        # trigger_webhooks()

        return {
            "output": output_file
        }, 200

api.add_resource(Root, '/')
api.add_resource(Concat, '/concat/')

if __name__ == '__main__':
    app.run(debug=True, port=9009)