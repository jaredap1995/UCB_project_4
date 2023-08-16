import psycopg2
from flask import Flask, render_template, jsonify
import pandas as pd
import json

#################################################
# Database Setup
#################################################

conn = psycopg2.connect(
    database="proj_4",
    user="postgres",
    password="123.Senco",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

################################################
# Flask Routes
#################################################

# Define a function to handle database transactions and errors
def execute_query(query, params=None):
    try:
        cur.execute(query, params)
        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

# Define a function to safely close the database connection
def close_connection():
    cur.close()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html') # Home page that has search engine/preferences and rotating images

@app.route('/load_chart')
def load_chart():
    try:
        # Retrieve data from PostgreSQL
        query = "SELECT manufacturer, year, AVG(price) AS avg_price FROM used_cars GROUP BY manufacturer, year ORDER BY manufacturer, year;"
        cur.execute(query)
        data = cur.fetchall()

        # print("data", data)

        # Calculate yearly price change and percentage change for each manufacturer
        chart_data = []
        for i in range(len(data)):
            if i > 0 and data[i][0] == data[i-1][0]:
                price_change = data[i][2] - data[i-1][2]
                percent_change = ((data[i][2] - data[i-1][2]) / data[i-1][2]) * 100 if data[i-1][2] != 0 else 0
                chart_data.append({
                    'manufacturer': data[i][0],
                    'year': int(data[i][1]),
                    'avg_price': float(data[i][2]),
                    'price_change': float(price_change),
                    'percent_change': float(percent_change)
                })

        return jsonify(chart_data)
    except Exception as e:
        print("Error:", e)
        return jsonify([])  # Return an empty list in case of an error

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    # Simulated results from the database...to be replaced by backend group work querying database
    results = [
        {'image': 'model_s.jpg', 'price': 100000, 'year': 2018, 'manufacturer': 'Tesla', 'model': 'Model S', 'id': 1, 'size': 'Any', 'condition': 'Any'},
        {'image': 'model_x.jpg', 'price': 50000, 'year': 2017, 'manufacturer': 'Tesla', 'model': 'Model X', 'id': 2, 'size': 'Any', 'condition': 'Any'},
        {'image': 'toyota.jpg', 'price': 75000, 'year': 2016, 'manufacturer': 'Toyota', 'model': 'Corolla', 'id': 3, 'size': 'Any', 'condition': 'Any'},
    ]

    reccomendations = [
        # ... (Your recommendation data)
    ]

    return render_template('results.html', results=results, reccomendations=reccomendations)

# @app.route('/car/<int:car_id>')
# def car_details(car_id):
#     # car = get_car_details(car_id) # Python functions that query the database for specific car details
#     # prediction = get_price_prediction(car_id)
#     return render_template('car.html', car=car)

@app.route('/get_chart_data')
def get_chart_data():
    # Retrieve data from the database and format it for the charts
    # Example data (replace this with actual data fetching and formatting)
    data = [
        {'make': 'Tesla', 'average_price': 60000},
        {'make': 'Toyota', 'average_price': 45000},
        {'make': 'Audi', 'average_price': 75000},
        # ...
    ]

    # Format data for charts
    chart_labels = [entry['make'] for entry in data]
    chart_data = [entry['average_price'] for entry in data]

    return jsonify({'labels': chart_labels, 'data': chart_data})

if __name__ == "__main__":
    app.run(debug=True)
