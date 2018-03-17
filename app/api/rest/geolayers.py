from flask import send_from_directory
from app.api.rest.base import BaseResource, SecureResource, rest_resource
import json


@rest_resource
class TestingTestTesting(BaseResource):
	""" /api/testing/testy """

	endpoints = ['/testing/testy']

	def get(self):
		print('getting data')
		return {'result': 'testing'}


@rest_resource
class geoData(BaseResource):
	""" /api/testing/testy """

	endpoints = ['/geodata/layers/<string:layer_type>']

	def get(self, layer_type):
		if layer_type == 'zip':
			print('zips worked')
			path = '../../../playground/data/'
			file = 'appdata_zips_180316.geojson'
			print(send_from_directory(path, file))
			# print(type(layer_type))
			return send_from_directory(path, file)

		if layer_type == 'coord':
			print('coords worked')
			path = '../../../playground/data/'
			file = 'appdata_coords_0316.geojson'
			return send_from_directory(path, file)
		
