import psycopg2
import json
from flask import Flask, jsonify, render_template, request
from datetime import datetime
import sys
import os

# utils 
import helpers as ht

#################################################
# Database Setup
#################################################

conn = psycopg2.connect(database="proj_4",
                            user="postgres",
                            password="postgres",
                            host="localhost",
                            port="5432")
cur = conn.cursor()



#################################################
# Flask Setup
#################################################

app = Flask(__name__)
app = Flask(__name__)

################################################
# Flask Routes
#################################################

"""
Home page that has search engine/preferences and rotating images
"""
@app.route('/')
def index():

    # assign DF to variable
    df = ht.get_df()
    
    # print(df)
    return render_template('index.html') 

@app.route('/team')
def team():
    return render_template('team.html') 

@app.route('/about')
def about():
    return render_template('about.html') #Make a page to describe the project

@app.route('/results', methods=["POST", "GET"])
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

    ##########################


    ########### Actual Code ################

    #Something Like
    """
    cursor.execute(select * from used_cars where price<20000 and price>100000 and 'year' > 2012)
    rows=cursor.fetchall()
    rows=pd.DataFrame(rows).tojson()
    return rows
    

    """
    """
    minPrice, maxPrice, condition, searchManufacturer
    """
    df = ht.get_df()
    # TODO get user input and filter the DF to a subset of the users attributes, render the results on results endpoint
    # try:
    #     search_bar = request.form.get('userInput')
    #     print('userInput from index.html: ', search_bar)
    # except ValueError:
    #      print()
    #########################################



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
    return render_template('car.html', car = car)

if __name__ == "__main__":
    # print("test", ht.get_df())
    app.run(debug=True)
