import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html') #Home page that has search engine/preferences and rotating images

@app.route('/about')
def about():
    return flask.render_template('about.html') #Make a page to describe the project

@app.route('/results')
def results():
    # Simulated results from the database...to be replaced by backend group work querying database
    ##### Sample Code ######
    results = [
        {'image': 'model_s.jpg', 'price': 100000, 'year': 2018, 'make': 'Tesla', 'model': 'Model S', 'id': 1},
        {'image': 'model_x.jpg', 'price': 50000, 'year': 2017, 'make': 'Tesla', 'model': 'Model X', 'id': 2},
        {'image': 'toyota.jpg', 'price': 75000, 'year': 2016, 'make': 'Toyota', 'model': 'Corrola', 'id': 3},
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

    #########################################



    return flask.render_template('results.html', results=results) #Webpage that gets results following search

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

    return flask.render_template('car.html', car = car)

if __name__ == "__main__":
    app.run(debug=True)