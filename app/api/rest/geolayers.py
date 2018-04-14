from flask import send_from_directory
# from app.api.rest.base import BaseResource, SecureResource, rest_resource
import json
from flask_restplus import Resource, abort, reqparse

from app.api import api_rest
from cartosight import GeoLayers
from cartosight import Explorer

g = GeoLayers()
e = Explorer()

@api_rest.route('/testing/testy')
class TestingTestTesting(Resource):
    """ /api/testing/testy """

    endpoints = []

    def get(self):
        print('getting data')
        return {'result': 'testing'}


@api_rest.route('/geodata/layers')
class geoData(Resource):
    """ /api/testing/testy """

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str, required=True,
                            help='Type required to retreive layers')
        parser.add_argument('column', type=str, required=False,
                            help='Desired column name required')
        args = parser.parse_args()

        if args['type'] == 'zip':
            return g.filter_zip(args['column'])
        if args['type'] == 'coordinates':
            return g.point_data(args['column'])


@api_rest.route('/geodata/column-names')
class columnNames(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('detail', type=str, required=True,
                            help='Detail required to retreive layers')
        args = parser.parse_args()
        return g.col_names(args['detail'])


@api_rest.route('/features/correlation')
class correlation(Resource):

    def get(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('detail', type=str, required=True,
        #                     help='Detail required to retreive layers')
        # args = parser.parse_args()
        return e.scatter()
