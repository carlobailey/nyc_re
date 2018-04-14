import geopandas as gpd
import pandas as pd
import os
import json
import datetime
from functools import lru_cache
from shapely.geometry import Point


class GeoLayers():

    def __init__(self):
        print('Retrieving geo data')        
        self.zip_data = gpd.read_file('playground/data/appdata_zips_180316.geojson')
        # self.zip_data = gpd.read_file('../playground/data/appdata_zips_180316.geojson')
        print('data received')


    def filter_zip(self, column):
        ''' Returns geojson of target column
        aggregated to zip code '''
        df = self.zip_data
        df = df[['ZIPCODE', 'geometry', column]]
        return df.to_json()


    def col_names(self, detail):
        if detail == 'zip':
            col_names = list(self.zip_data.columns)
        if detail == 'coordinates':
            col_names = ['price', 'total_lines', 'crimes']
        return json.dumps(col_names)

    def point_data(self, data_type):
        ''' Returns a GeoJSON of selected
        datatype '''
        if data_type == 'price':
            pt_data = pd.read_csv('playground/data/zillow_scraping/zillow_buy_with_coords.csv')
            pt_data['coordss'] = pt_data['coordss'].str.replace('\'','\"')
            geometry = pt_data['coordss'].apply(lambda x: json.loads(x)).tolist()
            geometry = [Point(x["lng"],x["lat"]) for x in geometry]
            df = pt_data[['zip', 'price', 'sqft', 'bedrooms', 'sale_type', 'coordss','address']]
            df = gpd.GeoDataFrame(df, geometry=geometry)
        if data_type == 'total_lines':
            pt_data = gpd.read_file('playground/data/subway-stations/Subway Stations.geojson')
            pt_data['total_lines'] = pt_data['line'].str.split('-').apply(lambda x: len(x))
            df = pt_data[['name', 'total_lines', 'geometry']]
        if data_type == 'crimes':
            df = pd.read_csv('playground/data/crime/crimes_with_zips.csv')
            df = df[df['zipcodes'].notnull()]
            relevant = ['BURGLARY','DANGEROUS WEAPONS','DANGEROUS DRUGS',
                'FELONY ASSAULT','ROBBERY','zipcodes']
            df = df[df['OFNS_DESC'].isin(relevant)]
            df = df[['OFNS_DESC','Latitude','Longitude']].sample(frac=0.1)
            geometry = [Point(x,y) for x,y in zip(df['Longitude'].tolist(),df['Latitude'].tolist())]
            df = gpd.GeoDataFrame(df, geometry=geometry)
        return df.to_json()

