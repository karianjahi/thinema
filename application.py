# import flask
from flask import Flask

# import function recommender
from recommender import recommend_movies

# tell flask this is the file where it launches from
app = Flask(__name__)

from flask import render_template
from flask import request
@app.route("/")
def index():
    return render_template("index.html")


# Create a function that takes the user to recommended movies
@app.route("/recommender")
def recommender():
    # We wish to capture the user input once they make a form submission on the browser
    # For this we need a module called request that captures the user input as a 
    # dictionary
    # Notice that in form tag, the input has a variable 'name'. This is the developers
    # secret variable to capture the input from the user
    # Once a submission is done, check the url in the browser
    # It has entries like movie1=3&movie2=4&movie3=1
    # We can capture these entries using the request.args attribute
    some_movies = dict(request.args)
    # Pass the movies to the recommender function for recommendations
    recs = recommend_movies(some_movies)
    # We render the recommender.html template but also make it dynamic
    # by carrying the movies variable
    return render_template("recommender.html", movies=recs)
# If you go to the recommender url (http://127.0.0.1:<port>/recommender) you should see the movies there


# To run and debug from only this script:
if __name__ == "__main__":
    app.run(debug=True, port=5000)