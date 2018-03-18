"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""

import time
from flask import request
# from app.api.rest.base import BaseResource, SecureResource, rest_resource
from flask_restplus import Resource, abort, reqparse

from app.api import api_rest, api_bp

@api_rest.route('/resource/one')
class ResourceOne(Resource):
    """ /api/resource/one """
    endpoints = []

    def get(self):
        time.sleep(1)
        return {'name': 'Resource One', 'data': True}

    def post(self):
        json_payload = request.json
        return {'name': 'Resource Post'}


@api_rest.route('/resource/two')
class SecureResourceOne(Resource):
    """ /api/resource/two """
    endpoints = []

    def get(self, resource_id):
        parser = reqparse.RequestParser()
        parser.add_argument('data', type=str, required=True,
                            help='this is a resource test')
        args = parser.parse_args()

        return {'name': 'Resource Two', 'data': args['data']}

