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
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    df['order_date'] = pd.to_datetime(df['order_date'])
    df.set_index('order_date', inplace=True)
    df['avg_item_sales'] = df.sales/df.quantity
    df['original_sales'] = df.sales + df.discount
    df['discount_percent'] = df.discount/df.original_sales * 100
    return df

def time_split(df):
    train = df[:'2015']
    validate = df['2016']
    test = df['2017':]
    return train, validate, test

