import geopandas as gpd
import os
import json
import datetime
from functools import lru_cache


class GeoLayers():

    def __init__(self):
        ''' Initialize connection to Redshift and get ALL data'''
        print('Retrieving geo data')        
        self.zip_data = gpd.read_file('playground/data/appdata_zips_180316.geojson')
        # self.zip_data = gpd.read_file('../playground/data/testfile.geojson')
        print('data received')


    def filter_zip(self, column):
        ''' Returns geojson of target column
        aggregated to zip code '''
        df = self.zip_data
        df = df[['ZIPCODE', 'geometry', column]]
        return df.to_json()
