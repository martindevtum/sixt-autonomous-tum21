from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
import apiInterfaces.sixtRequests.bookings as bookings
import apiInterfaces.sixtRequests.vehicles as vehicles




# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

# get all vehicles
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/vehicles', methods=['GET'])
def all_vehicles():
    return { 'allVehicles': vehicles.get_all() }

@app.route('/bookings', methods=['GET'])
def all_bookings():
   return { 'allBookings': bookings.get_all() }

@app.route('/bookings/delete/<item_id>', methods=['GET'])
def delete_booking(item_id):
    bookings.delete(item_id)
    return { 'message': 'success' } 

if __name__ == '__main__':
    app.run()
