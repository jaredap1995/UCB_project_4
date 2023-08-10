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
    return flask.render_template('results.html') #Webpage that gets results following search

if __name__ == "__main__":
    app.run(debug=True)