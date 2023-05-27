from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/save-data', methods=['POST'])
def save_data():
    req = request.get_json()
    if not req:
        return {
            'message': 'Bad request'
        }, 400

    # Save data to database
    # ...

    return {
        'message': 'Data saved successfully'
    }, 200

@app.route('/get-data', methods=['GET'])
def get_data():
    req = request.get_json()
    if not req:
        return {
            'message': 'Bad request'
        }, 400

    # Get data from database
    # ...
    
    data = None
    if not data:
        return {
            'message': 'Data not found'
        }, 404
    return {
        'status': 200,
        'message': 'Data retrieved successfully'
    }, 200