# import flask
from flask import Flask

# tell flask this is the file where it launches from
app = Flask(__name__)

# Create a function that displays 'hello world' on our home page
# The @app decorator tells the function the path to launch from
# "/" means lauching from the home page

# Instead of writing html code inside our python code, we could create a templates folder
# This folder shall carry all html content that we wish to display on a webpage
# We shall also change the hello_word which is our homepage function to index which is the default
# in the templates, we create a file index.html which carry the home page content
# Since templates are now separate, we have to render them. We have to import the 
# module render_template
# render_template can take any no. *args e.g. berlin="berlin", name="samson" etc
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
    print(some_movies)
    # We render the recommender.html template but also make it dynamic
    # by carrying the movies variable
    return render_template("recommender.html", movies=some_movies)
# If you go to the recommender url (http://127.0.0.1:<port>/recommender) you should see the movies there


# To run and debug from only this script:
if __name__ == "__main__":
    app.run(debug=True, port=5000)