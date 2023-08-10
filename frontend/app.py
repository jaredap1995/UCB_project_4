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
    results = [
        {'image': 'model_s.jpg', 'price': 100000, 'year': 2018, 'make': 'Tesla', 'model': 'Model S'},
        {'image': 'model_x.jpg', 'price': 50000, 'year': 2017, 'make': 'Tesla', 'model': 'Model X'},
        {'image': 'toyota.jpg', 'price': 75000, 'year': 2016, 'make': 'Toyota', 'model': 'Corrola'},
    ]
    return flask.render_template('results.html', results=results) #Webpage that gets results following search

if __name__ == "__main__":
    app.run(debug=True)