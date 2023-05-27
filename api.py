from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.get_json()

    # Save data to database
    # ...

    return {
        'message': 'Data saved successfully',
        'data': data,
    }, 200

@app.route('/get-data', methods=['GET'])
def get_data():
    return {
        'message': 'Data retrieved successfully',
    }, 200