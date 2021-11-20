import requests
import json

with open('config.json') as f:
    api_endpoint = json.load(f).get("api_endpoint")

# get all bookings
def get_all():
    return use_api('GET', f'bookings')

# get booking by id
def get_by_id(id):
    return use_api('GET', f'bookings/{id}')

# create a booking
def create(booking):
    return use_api('POST', f'bookings', data=booking)

# delete booking
def delete(id):
    return use_api('DELETE', f'bookings/{id}')

# assign vehicle to booking
def assign(vehicleId, bookingId):
    return use_api('POST', f'bookings/{bookingId}/assignVehicle/{vehicleId}')

# set passenger is on
def passenger_got_on(id):
    return use_api('POST', f'bookings/{id}/passengerGotOn')

def passenger_got_off(id):
    return use_api('POST', f'bookings/{id}/passengerGotOff')

def use_api(method, api_path, data=None):
    req = requests.Request(method, f'{api_endpoint}/{api_path}', data=data)
    r = req.prepare()

    s = requests.Session()
    resp = s.send(r)

    return resp.json
