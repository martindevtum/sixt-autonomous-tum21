from flask import Flask, jsonify
from flask_cors import CORS

import sys 
import os
sys.path.append(os.path.abspath("requests/sixtRequests"))

import bookings
import vehicles

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# get all vehicles
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/vehicles', methods=['GET'])
def all_vehicles():
    return { 'allVehicles': vehicles.getAllVehicles().json() }

@app.route('/bookings', methods=['GET'])
def all_bookings():
    return { 'allBookings': bookings.getAllBookings().json() }

if __name__ == '__main__':
    app.run()
