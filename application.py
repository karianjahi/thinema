# import flask
from flask import Flask

# tell flask this is the file where it launches from
app = Flask(__name__)

# Create a function that displays 'hello world' on our home page
# The @app decorator tells the function the path to launch from
# "/" means lauching from the home page

@app.route("/")
def hello_world():
    # Introduce html tags. Here we want to make hello world a header h1
    return '<h1>hello world</h1>'


# Create a function that takes the user to recommended movies
@app.route("/recommender")
def recommender():
    some_movies = ["movie1", "movie2", "movie3"]
    return f'{some_movies}'

# If you go to the recommender url (http://127.0.0.1:<port>/recommender) you should see the movies there


# To run and debug from only this script:
if __name__ == "__main__":
    app.run(debug=True, port=5000)