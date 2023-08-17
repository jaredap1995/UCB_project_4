import psycopg2
import json
from flask import Flask, jsonify, render_template, request
from datetime import datetime
import sys
import os
import pandas as pd
from helper import get_image_url

#################################################
# Database Setup
#################################################

conn = psycopg2.connect(database="proj_4",
                            user="postgres",
                            password="Ulysses@5280+", #password="postgres"
                            host="localhost",
                            # port = "5432"
                            port="5433"
                            )
cur = conn.cursor()




#################################################
# Flask Setup
#################################################

app = Flask(__name__)

################################################
# Flask Routes
#################################################

@app.route('/')
def index():
    return render_template('index.html') #Home page that has search engine/preferences and rotating images

@app.route('/team')
def team():
    return render_template('team.html') 

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/results', methods=['GET','POST'])
def results():
    # https://stackoverflow.com/questions/60620082/importing-a-dataframe-from-one-jupyter-notebook-into-another-jupyter-notebook
    # Importing Dataframe from car_reccomender and elasticent_regression
    rec_df = pd.read_pickle("recommended_cars.pkl") # 3 cars reccomended from car_recommender
    # sel_df = pd.read_pickle("selected_cars.pkl") # 1 car selected from car_recommender

    # importing Dataframe from elacticnet regression
    # elas_df = pd.read_pickle("[FILENAME.pkl]")



    ########### Actual Code ################
    # Target the `name` attribute in each select element from index.html
    state = request.form.get('state')
    maxPriceRange = int(request.form.get('maxPriceRange'))
    condition = request.form.get('condition')
    manufacturer = request.form.get('manufacturer')
    size = request.form.get('size')
    odometer = int(request.form.get('odometer').split()[-1])
    transmission = request.form.get('transmission')
    cylinder = request.form.get('cylinder')
    conditions = [state, maxPriceRange, condition, manufacturer, size, odometer, transmission, cylinder]

    # #Base query
    # base_query = 'select * from used_cars where 1=1;'
    # params=[]
    # for param in conditions:
    #     if param and param != "Any":
    #         base_query += " AND %s "

    search_query = """SELECT * FROM used_cars WHERE
                 price < %s AND
                 manufacturer = %s AND
                 condition >= %s AND 
                 odometer <= %s AND 
                 size = %s AND
                 state = %s"""

    cur.execute(search_query, (maxPriceRange, manufacturer, condition, odometer, size, state))
    columns=["price", "year","manufacturer","condition","cylinders","fuel","odometer","title_status","transmission","drive","size","type","paint_color","state","posting_date", 'id']

    results=cur.fetchall()
    # print(results)
    results=pd.DataFrame(results, columns=columns)
    results.columns=columns
    results=[results.iloc[s].to_dict() for s in range(len(results))]
    for i in range(len(results)):
        results[i]['image']='hello.com'
        results[i]['odometer']=int(results[i]['odometer'])
        results[i]['price']=int(results[i]['price'])


    #########################################
    # Sql query for user selection on car.html
    # search_q = f"SELECT * FROM used_cars WHERE state = {state} AND price < {maxPriceRange} AND condition >= {condition} AND manufacturer = {manufacturer} \
    #                         and size = {size} and miles <= {odometer}"
   
    
    #https://stackoverflow.com/questions/902408/how-to-use-variables-in-sql-statement-in-python

    return render_template('results.html', results=results) #Webpage that gets results following search

@app.route('/car/<int:car_id>') #'/<int:car_id>'
def car_details(car_id):
    
    #Something Like
    cur.execute(f"Select * from used_cars where id = {car_id}")
    car=cur.fetchone()
    if not car:
        return ValueError()
    columns=["price", "year","manufacturer","condition","cylinders","fuel","odometer","title_status","transmission","drive","size","type","paint_color","state","posting_date", 'id']
    car=pd.Series(car, index = columns).to_dict()
    query = f"{car['year']} {car['manufacturer']} {car['size']} {car['type']}"
    car['image'] = get_image_url(query)
    print(car['image'])

    reccomendations=0 ##Code Here that will fire up the model and get a reccomendation for the car based on parameters

    return render_template('car.html', car = car, reccomendations=reccomendations)

if __name__ == "__main__":
    app.run(debug=True)
