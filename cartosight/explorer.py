import pandas as pd
import json

class Explorer():

    def __init__(self):
        print('Retrieving features data')        
        self.feature_data = pd.read_csv('playground/data/features_180310.csv')
        # self.feature_data = pd.read_csv('../playground/data/features_180310.csv')
        # self.zip_data = gpd.read_file('../playground/data/appdata_zips_180316.geojson')
        print('data received')


    def scatter(self, column):
        df = self.feature_data
        df = df[['price', column]].sample(frac=0.25)
        df.rename(columns={'price': 'x', column: 'y'},inplace=True)
        return json.dumps(df.to_dict(orient='records'))
