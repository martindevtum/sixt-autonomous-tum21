import requests
import json

with open('config.json') as f:
    api_endpoint = json.load(f).get("api_endpoint")

# get all vehicles
def get_all():
    return use_api('GET', f'vehicles')

# get specific vehicle
def get_by_id(id):
    return use_api('GET', f'vehicles/{id}')

# update vehicle location withID
def update_location(id, newLocation):
    return use_api('POST', f'vehicles/{id}/coordinates/', data=newLocation)

# update vehicle location newCharge
def update_charge(id, newCharge):
    return use_api('POST', f'vehicles/{id}/charge/', data=newCharge)

# block vehicle by id
def block(id):
    return use_api('POST', f'vehicles/{id}/block/')

# unblock vehicle by id
def unblock(id):
    return use_api('POST', f'vehicles/{id}/unblock/')

def use_api(method, api_path, data=None):
    req = requests.Request(method, f'{api_endpoint}/{api_path}', data=data)
    r = req.prepare()

    s = requests.Session()
    resp = s.send(r)

    return resp.json()
