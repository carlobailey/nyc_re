""" API Blueprint Application """

import os
from flask import Flask, Blueprint, session
from flask_restplus import Api

api_bp = Blueprint('api_bp', __name__,
                   template_folder='templates',
                   url_prefix='/api',
                   static_folder='static')

api_rest = Api(api_bp, doc='/docs/',
               version='0.1.0',
               description='NYC RE API')

#OPTIONAL
@api_bp.after_request
def add_header(response):
    # Required for vue app served from localhost to access 127.0.0.1:5000
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

from app.api import views
from app.api.rest import routing, geolayers

