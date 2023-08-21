import psycopg2
import json
import numpy as np
from flask import Flask, jsonify, render_template, request
from datetime import datetime, timedelta
import sys
import os
import pandas as pd
from helper import get_image_url
import smtplib
from email.message import EmailMessage
from recommender import recommendation_model
from helper import get_df


#################################################
# Database Setup
#################################################

conn = psycopg2.connect(database="proj_4", #project_4
                            user="postgres", #postgres
                            password="postgres", #password="postgres"
                            host="localhost",
                            port = "5432"
                            # port="5433"
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
    # get list of matrix for our line data and send it to about page
    chart_data = load_chart()
    # print('TEST chart_data:',chart_data)
    return render_template('about.html', chart_data=chart_data)


@app.route('/results', methods=['GET','POST'])
def results():
    # https://stackoverflow.com/questions/60620082/importing-a-dataframe-from-one-jupyter-notebook-into-another-jupyter-notebook
    # Importing Dataframe from car_reccomender and elasticent_regression

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
    filters = {
        'state': state.lower(),
        'price': maxPriceRange,
        'condition': condition.lower(),
        'manufacturer': manufacturer.lower(),
        'size': size.lower(),
        'odometer': odometer,
        'transmission': transmission.lower(),
        'cylinders': cylinder.lower(),
    }

    numerical_conditions = {
        'price': '<=',
        'odometer': '<='
    }



    #Base query....create a query that is always true
    base_query = 'select * from used_cars where 1=1'


    params=[]
    for column, value in filters.items():
        if value != "any":
            if column in numerical_conditions:
                base_query +=f" AND {column} {numerical_conditions[column]} {value}"
            else:
                base_query += f" AND {column} = '{value}'"
            params.append(value)
        else:
            base_query+=''

    cur.execute(base_query, params)
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
    
    columns=["price", "year","manufacturer","condition","cylinders","fuel","odometer","title_status","transmission","drive","size","type","paint_color","state","posting_date", 'id']
    # cur.execute(f"Select * from used_cars")
    # data=cur.fetchall()
    # data=pd.DataFrame(data, columns=columns)
    # data['price']=data['price'].astype('int')
    reccomendations, price_prediction = recommendation_model(car_id)
    price_prediction={'prediction': price_prediction}
    # print(reccomendations) #This successfully pulls the reccomendations

    #Query for main result
    cur.execute(f"Select * from used_cars where id = {car_id}")
    car=cur.fetchone()
    if not car:
        return ValueError()
    car=pd.Series(car, index = columns).to_dict()
    car['price']=int(car['price'])
    price_prediction['percent_error']=abs(np.round(((car['price']-price_prediction['prediction'])/car['price'])*100, decimals=1))
    query = f"{car['year']} {car['manufacturer']} {car['size']} {car['type']}"
    car['image'] = get_image_url(query)

    return render_template('car.html', car = car, reccomendations=reccomendations, price_prediction=price_prediction)

# Fn to return a matrix of lists for line plot data on /about route
def load_chart():
    # Retrieve data from PostgreSQL
    selected_manufacturers = ['toyota', 'nissan', 'tesla', 'bmw', 'audi', 'mazda', 'volvo', 'mercedes-benz','acura', 'ford']
    manufacturer_string = ', '.join([f"'{manufacturer}'" for manufacturer in selected_manufacturers])
    # Calculate the date 12 years ago from today
    ten_years_ago = datetime.now() - timedelta(days=365 * 12)
    ten_years_ago_year = ten_years_ago.year
    # Calculate the start and end years for the desired range (2012-2023)
    start_year = 2012
    end_year = min(datetime.now().year, 2023)  # Use the current year if it's before 2023
    query = f"""
        SELECT manufacturer, year, AVG(price) AS avg_price,
               COALESCE((AVG(price) - LAG(AVG(price), 1) OVER (PARTITION BY manufacturer ORDER BY year)), 0) AS price_change,
               COALESCE((AVG(price) - LAG(AVG(price), 1) OVER (PARTITION BY manufacturer ORDER BY year)) / LAG(AVG(price), 1) OVER (PARTITION BY manufacturer ORDER BY year) * 100, 0) AS percent_change
        FROM used_cars
        WHERE manufacturer IN ({manufacturer_string}) AND year BETWEEN {start_year} AND {end_year}
        GROUP BY manufacturer, year
        ORDER BY manufacturer, year;
    """
    cur.execute(query)
    data = cur.fetchall()
    chart_data = {}
    for manufacturer in selected_manufacturers:
        chart_data[manufacturer] = {'year': [], 'avg_price': [], 'price_change': [], 'percent_change': []}
    for i in range(len(data)):
        manufacturer = data[i][0]
        year = int(data[i][1])
        avg_price = float(data[i][2])
        price_change = float(data[i][3])
        percent_change = float(data[i][4])
        chart_data[manufacturer]['year'].append(year)
        chart_data[manufacturer]['avg_price'].append(avg_price)
        chart_data[manufacturer]['price_change'].append(price_change)
        chart_data[manufacturer]['percent_change'].append(percent_change)
    return chart_data

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    recipient_email = data['email']

    SMTP_USER = 'jaredaperez1995@gmail.com'
    SMTP_PASSWORD = 'y3AQcTnf1hNE7t4G'
    SMTP_PORT=587
    SMTP_SERVER= 'smtp-relay.brevo.com'

    msg = EmailMessage()
    msg.set_content('You have successfully signed up for updates.')
    msg['Subject'] = 'Thank you for signing up!'
    msg['From'] = SMTP_USER
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        return jsonify(message='Email sent successfully'), 200
    except Exception as e:
        print(e)
        return jsonify(message='Failed to send email.'), 400

if __name__ == "__main__":
    app.run(debug=True)
