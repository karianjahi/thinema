# import flask
from flask import Flask

# tell flask this is the file where it launches from
app = Flask(__name__)

# Create a function that displays 'hello world' on our home page
# The @app decorator tells the function the path to launch from
# "/" means lauching from the home page

@app.route("/")
def hello_world():
    return 'hello world'


# To run and debug from only this script:
if __name__ == "__main__":
    app.run(debug=True, port=5000)