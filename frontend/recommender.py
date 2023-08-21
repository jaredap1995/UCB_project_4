#import
import pandas as pd
import pickle 
import psycopg2
import hvplot.pandas
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

def load_data():
    conn = psycopg2.connect(database="proj_4",
                            user="postgres",
                            password="postgres", #password="postgres"
                            host="localhost",
                            port = "5432")
    cur = conn.cursor()

    sql_query = '''Select * From used_cars'''
    cur.execute(sql_query)

    results=cur.fetchall()
    columns=["price", "year","manufacturer","condition","cylinders","fuel","odometer","title_status","transmission","drive","size","type","paint_color","state","posting_date", 'id']
    results=pd.DataFrame(results, columns=columns)
    
    return results

#main df
# cars_df = load_data()

def model_cleaning(cars_df):

    # dropping duplicates
    duplicate_cols = ['price', 'year', 'manufacturer', 'condition', 'cylinders', 'fuel', 'odometer', 'title_status', 'transmission', 'drive', 'size', 'type', 'paint_color', 'state']
    cars_df = cars_df.drop_duplicates(subset=duplicate_cols)

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
    
    new_df = regr_cars_df

    #2nd cell ~ Cleaning
    # Scaling price and odometer data
    columns_to_scale = ['price', 'odometer']
    features = regr_cars_df[columns_to_scale]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    regr_cars_df[columns_to_scale] = scaled_features
    
    return regr_cars_df, new_df

#cleaned datafram
# regr_cars_df = model_cleaning()

def model_training(regr_cars_df):

    model_knn = NearestNeighbors(metric='cosine', algorithm='auto', n_neighbors=20, n_jobs=1) # n_jobs can be adjusted based on number of cores

    # Fit the model
    model_knn.fit(regr_cars_df)

    # Its important to use binary mode 
    knnPickle = open('frontend/model_saves/car_recommend', 'wb') #Adjust to `frontend/model_saves/car_recommend` according to situations
        
    # source, destination 
    pickle.dump(model_knn, knnPickle)  

    # close the file
    knnPickle.close()

    return model_knn


def model_load():
    # load the model from disk
    return pickle.load(open('model_saves/car_recommend', 'rb')) #Add frontend
    
def recommendation_model(car_id):
    cars_df = load_data()
    regr_cars_df, new_df = model_cleaning(cars_df)

    X = new_df.drop(['price', 'id'], axis =1).values
    filename = 'frontend/model_saves/regression_model.pkl'
    loaded_model = pickle.load(open(filename, 'rb'))
    input = X[car_id].reshape(1,56)
    predicted_price = int(loaded_model.predict(input)[0])
    # predicted_price=47000
    # print(f"This is the predicted price {predicted_price}")

    model_knn= model_training(regr_cars_df)


    selected_car = regr_cars_df.iloc[car_id].values.reshape(1, -1)

    distances, indices = model_knn.kneighbors(selected_car, n_neighbors=4)

    recommended_cars = cars_df.iloc[indices[0]]

    demo_dict = pd.DataFrame(recommended_cars[['id','price','year','manufacturer', 'fuel', 'title_status', 'type', 'paint_color', 'state', 'transmission', 'drive', 'condition', 'size', 'odometer']][1:4])
    # demo_dict = demo_dict.reset_index()
    demo_dict = demo_dict.to_dict(orient='records')

    return demo_dict, predicted_price


