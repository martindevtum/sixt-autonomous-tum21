from flask import Flask, jsonify
from flask_cors import CORS

import sys
import os
import json

import apiInterfaces.sixtRequests.bookings as bookings
import apiInterfaces.sixtRequests.vehicles as vehicles

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
    return { 'allVehicles': json.dumps(vehicles.get_all()) }

@app.route('/bookings', methods=['GET'])
def all_bookings():
   return { 'allBookings': json.dumps(bookings.get_all()) }

if __name__ == '__main__':
    app.run()
