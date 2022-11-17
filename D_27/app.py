""" My first api with Python, Flask """

from flask import Flask, request

database = {'rasel': 150}

# Initialize flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Welcome to my first web api"


@app.route('/getdata/', methods=['GET'])
def get_data():
    return database


@app.route('/adddata/', methods=['GET', 'PUT'])
def add_data():
    key, value = list(request.args.items())[0]
    database[key] = value
    return f"{key} added"


@app.route('/deletedata/', methods=['GET', 'DELETE'])
def delete_data():
    key, value = list(request.args.items())[0]
    database.pop(value)
    return f"{value} Deleted"


if __name__ == '__main__':
    app.run()
