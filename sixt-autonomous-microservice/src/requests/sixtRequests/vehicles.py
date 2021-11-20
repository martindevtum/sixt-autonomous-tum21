import requests

# get all vehicles
def getAllVehicles():
    return requests.get('https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api/vehicles/')

# get specific vehicle
def getVehicleById(id):
    return requests.get(f'https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api/vehicles/{id}')

# update vehicle location withID
def updateVehicleLocationById(id, newLocation):
    return requests.post(f'https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api/vehicles/{id}/coordinates/', data=newLocation)

# update vehicle location newCharge
def updateVehicleChargeById(id, newCharge):
    return requests.post(f'https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api/vehicles/{id}/charge/', data=newCharge)

# block vehicle by id
def blockVehicleById(id):
    return requests.post(f'https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api/vehicles/{id}/block/')

# unblock vehicle by id
def unblockVehicleById(id):
    return requests.post(f'https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api/vehicles/{id}/unblock/')
