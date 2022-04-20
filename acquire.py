from env import username, password, host
import os
import pandas as pd
import numpy as np


def get_superstore_data(use_cache=True):
    filename = "superstore.csv"
    if os.path.isfile(filename) and use_cache:
        print("Let me get that for you...")
        return pd.read_csv(filename)
    print("Sorry, nothing on file, let me create one for you...")
    data = 'superstore_db'
    url = f'mysql+pymysql://{username}:{password}@{host}/{data}'
    query = '''
    SELECT *
        FROM orders
        JOIN categories USING (`Category ID`)
        JOIN customers USING (`Customer ID`)
        JOIN products USING (`Product ID`)
        JOIN regions USING (`Region ID`);
    '''
    df = pd.read_sql(query, url)
    df.to_csv(filename)
    return df

    def prep_superstore_data(df):
        df.drop(columns=['Unnamed: 0', 'Region ID', 'Product ID', 'Customer ID', 'Category ID', 'Country'], inplace=True)
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        df.set_index('Order Date', inplace=True)
        df.columns = df.columns.str.replace(' ', '_').str.lower()
        return df