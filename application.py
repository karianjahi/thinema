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
@app.route("/")
def index():
    # Introduce html tags. Here we want to make hello world a header h1
    return render_template("index.html")


# Create a function that takes the user to recommended movies
@app.route("/recommender")
def recommender():
    some_movies = ["movie1", "movie2", "movie3"]
    # We render the recommender.html template but also make it dynamic
    # by carrying the movies variable
    return render_template("recommender.html", movies=some_movies)
# If you go to the recommender url (http://127.0.0.1:<port>/recommender) you should see the movies there


# To run and debug from only this script:
if __name__ == "__main__":
    app.run(debug=True, port=5000)