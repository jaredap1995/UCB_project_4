import psycopg2
import json
from flask import Flask, jsonify, render_template, request
from datetime import datetime
import sys
import os
import pandas as pd

#################################################
# Database Setup
#################################################

conn = psycopg2.connect(database="proj_4",
                            user="postgres",
                            password="postgres", #password="Ulysses@5280+" ~~ Kyle Password
                            host="localhost",
                            port="5432"
                            # port = "5433" Kyle Port
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
    # Simulated results from the database...to be replaced by backend group work querying database
    ##### Sample Code ######
    results = [
        {'image': 'model_s.jpg', 'price': 100000, 'year': 2018, 'manufacturer': 'Tesla', 'model': 'Model S', 'id': 1, 'size': 'Any', 'condition': 'Any'},
        {'image': 'model_x.jpg', 'price': 50000, 'year': 2017, 'manufacturer': 'Tesla', 'model': 'Model X', 'id': 2, 'size': 'Any', 'condition': 'Any'},
        {'image': 'toyota.jpg', 'price': 75000, 'year': 2016, 'manufacturer': 'Toyota', 'model': 'Corrola', 'id': 3, 'size': 'Any', 'condition': 'Any'},
    ]

    reccomendations = [
         {'image': 'audi7.jpg', 'price': 100000, 'year': 2018, 'manufacturer': 'Audi', 'model': 'A7', 'id': 4, 'size': 'Any', 'condition': 'Any'},
        {'image': 'gwagon.jpg', 'price': 50000, 'year': 2017, 'manufacturer': 'Mercedez', 'model': 'G Wagon', 'id': 5, 'size': 'Any', 'condition': 'Any'},
        {'image': 'vwcc.jpg', 'price': 75000, 'year': 2016, 'manufacturer': 'Volkswagen', 'model': 'CC', 'id': 6, 'size': 'Any', 'condition': 'Any'},
         {'image': 'audi7.jpg', 'price': 100000, 'year': 2018, 'manufacturer': 'Audi', 'model': 'A7', 'id': 4, 'size': 'Any', 'condition': 'Any'},
        {'image': 'gwagon.jpg', 'price': 50000, 'year': 2017, 'manufacturer': 'Mercedez', 'model': 'G Wagon', 'id': 5, 'size': 'Any', 'condition': 'Any'},
        {'image': 'vwcc.jpg', 'price': 75000, 'year': 2016, 'manufacturer': 'Volkswagen', 'model': 'CC', 'id': 6, 'size': 'Any', 'condition': 'Any'},
    ]
    # https://stackoverflow.com/questions/60620082/importing-a-dataframe-from-one-jupyter-notebook-into-another-jupyter-notebook
    # Importing Dataframe from car_reccomender and elasticent_regression
    rec_df = pd.read_pickle("recommended_cars.pkl") # 3 cars reccomended from car_recommender
    sel_df = pd.read_pickle("selected_cars.pkl") # 1 car selected from car_recommender

    # importing Dataframe from elacticnet regression
    # elas_df = pd.read_pickle("[FILENAME.pkl]")

    
    
    ##########################


    ########### Actual Code ################
    # Target the `name` attribute in each select element from index.html
    state = request.form.get('state')
    maxPriceRange = request.form.get('maxPriceRange')
    condition = request.form.get('condition')
    manufacturer = request.form.get('manufacturer')
    size = request.form.get('size')
    odometer = request.form.get('odometer')
    transmission = request.form.get('transmission')
    cylinder = request.form.get('cylinder')
    print(state, maxPriceRange, condition, manufacturer, size, odometer, transmission, cylinder)
    #  return f"Selected values: Dropdown 1: {dropdown1_value}, and {state}"
    #Something Like
    """
    cursor.execute(select * from used_cars where price<20000 and price>100000 and 'year' > 2012)
    rows=cursor.fetchall()
    rows=pd.DataFrame(rows).tojson()
    return rows
    

    """

    #########################################
    # Sql query for user selection on car.html
    # search_q = f'''SELECT * FROM used_cars WHERE state = {state} AND price < {maxPriceRange} AND condition > {condition} AND manufacturer = {manufacturer} \
    #                         and size = {size} and miles < {odometer}'''
    #     rows=cur.fetchmany(4)
    #     rows=pd.DataFrame(rows).tojson()
    #     return rows
    
    #https://stackoverflow.com/questions/902408/how-to-use-variables-in-sql-statement-in-python

    return render_template('results.html', results=results, reccomendations=reccomendations) #Webpage that gets results following search

@app.route('/car/<int:car_id>') #'/<int:car_id>'
def car_details(car_id):
    # car = get_car_details(car_id) #Python functions that queries database for specific car and returns the details. Car_id=unique id of car in database
    # prediction = get_price_prediction(car_id)
    
    ########### Sample Code #########
    results = [
        {'image': 'model_s.jpg', 'price': 100000, 'year': 2018, 'make': 'Tesla', 'model': 'Model S', 'id': 1},
        {'image': 'model_x.jpg', 'price': 50000, 'year': 2017, 'make': 'Tesla', 'model': 'Model X', 'id': 2},
        {'image': 'toyota.jpg', 'price': 75000, 'year': 2016, 'make': 'Toyota', 'model': 'Corrola', 'id': 3},
    ]

    for val in results:
            if val['id']==car_id:
                car=val
    #################################


    ###### ----- Actual code ------ #############
    
    #Something Like
    """
    cursor.execute(Select * from used_cars where id = car_id returning blah blah)
    rows=cursor.fetchall()
    rows=pd.DataFrame(rows).todict()/json
    car=rows
    """
    #################################

    return render_template('car.html', car = car)

if __name__ == "__main__":
    app.run(debug=True)
