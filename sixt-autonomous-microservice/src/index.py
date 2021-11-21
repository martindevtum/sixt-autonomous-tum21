from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
import apiInterfaces.sixtRequests.bookings as bookings
import apiInterfaces.sixtRequests.vehicles as vehicles
import sixtFunctions.carFinder as carFinder



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

@app.route('/bookings/create', methods=['POST'])
def create_booking():
    post_data = request.get_json()
    bookings.create(post_data)
    return { 'message': 'success' } 

@app.route('/bookings/<booking_id>/assignVehicle/<vehicle_id>', methods=['POST'])
def assign_vehicle_to_booking(booking_id, vehicle_id):
    bookings.assign(vehicle_id, booking_id)
    return { 'message': 'success' } 

@app.route('/bookings/<booking_id>/passengerGotOn', methods=['POST'])
def passenger_got_on(booking_id):
    bookings.passenger_got_on(booking_id)
    return { 'message': 'success' } 

@app.route('/bookings/<booking_id>/passengerGotOff', methods=['POST'])
def passenger_got_off(booking_id):
    bookings.passenger_got_off(booking_id)
    return { 'message': 'success' } 

@app.route('/bookings/vehicles/<pickupPoint>', methods=['GET'])
def get_vehicles_for_booking(pickupPoint):
    return { 'bestVehicles': carFinder.find_best_cars(pickupPoint) }

if __name__ == '__main__':
    app.run()
