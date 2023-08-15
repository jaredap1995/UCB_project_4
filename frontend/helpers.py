# %%

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import psycopg2
from sklearn.preprocessing import OrdinalEncoder
from sqlalchemy import create_engine
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings('ignore')

def get_df():

    # engine = create_engine('postgresql://postgres:postgres@localhost/proj_4')
    engine = psycopg2.connect('postgresql://postgres:postgres@localhost/proj_4')

    cars_df = pd.read_sql('select * from used_cars', engine)

    cars_df = cars_df[cars_df['price'] < 100000].copy()

    # nominal encoder
    top_manufacturers = cars_df['manufacturer'].value_counts()[cars_df['manufacturer'].value_counts() > 500].index.values
    cars_df = cars_df[cars_df['manufacturer'].isin(top_manufacturers)].copy()
    # combine dummy variables with DataFrame
    cars_df = pd.concat([cars_df,pd.get_dummies(cars_df['manufacturer'], dtype=float)], axis=1)

    # convert categorical data appropriately for sklearn
    cars_df['condition'] = cars_df['condition'].map({'salvage':0,
                            'fair':1,
                            'good':2,
                            'excellent':3,
                            'like new':4,
                            'new':5})

    cars_df = cars_df[cars_df['cylinders'] != 'other']
    cars_df['cylinders'] = cars_df['cylinders'].map({'3 cylinders':0,
                                                    '4 cylinders':1,
                                                    '5 cylinders':2,
                                                    '6 cylinders':3,
                                                    '8 cylinders':4,
                                                    '10 cylinders':5,
                                                    '12 cylinders':6})

    # combine dummy variables with DataFrame
    cars_df = pd.concat([cars_df, pd.get_dummies(cars_df['fuel'], dtype=float)], axis=1)
    # convert nominal categorical data
    cars_df = pd.concat([cars_df, pd.get_dummies(cars_df['title_status'], dtype=float)], axis=1)

    # transmission value other not useful, drop it
    cars_df = cars_df[cars_df['transmission'] != 'other'].copy()
    # convert nominal categorical data
    cars_df = pd.concat([cars_df, pd.get_dummies(cars_df['transmission'], dtype=float)], axis=1)

    # convert nominal categorical data
    cars_df = pd.concat([cars_df, pd.get_dummies(cars_df['drive'], dtype=float)], axis=1)

    #encode size to be numeric
    cars_df['size'] = cars_df['size'].map({'sub-compact':0, 'compact':1, 'mid-size':2, 'full-size':3})

    # convert only the types with values counts > 400
    type_cars = ['sedan', 'SUV', 'truck', 'pickup', 'coupe', 'hatchback', 'van', 'convertible', 'mini-van', 'wagon']
    cars_df = cars_df[cars_df['type'].isin(type_cars)].copy()
    cars_df = pd.concat([cars_df, pd.get_dummies(cars_df['type'], dtype=float)], axis=1)

    regr_cars_df = cars_df.drop(columns=['manufacturer', 'fuel', 'title_status', 'type', 'paint_color', 'state', 'posting_date', 'transmission', 'drive']).copy()

    # regr_cars_df.info()
    # print('regr_cars_df\n',regr_cars_df)
    # regr_cars_df.info()
    return regr_cars_df

if __name__=='__main__':
    pass
# %%
