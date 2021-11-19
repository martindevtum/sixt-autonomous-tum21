import requests

# get all bookings
def getAllbookings():
    return requests.get('https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api/bookings')

# get booking by id
def getBookingById(id):
    return requests.get(f'https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api/bookings/{id}')

# create a booking
def createBooking(booking):
    return requests.post('https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api/bookings', data=booking)

# delete booking
def deleteBookingById(id):
    return requests.delete(f'https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api/bookings/{id}')

# assign vehicle to booking
def assignVehicleToBookingById(bookingId, vehicleId):
    return requests.post(f'https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api//bookings/{bookingId}/assignVehicle/{vehicleId}') 

# set passenger is on
def setPassengerIsOnById(id):
    return requests.post(f'https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api//bookings/{id}/passengerGotOn')

def setPassengerIsOffById(id):
    return requests.post(f'https://us-central1-sixt-hackatum-2021.cloudfunctions.net/api//bookings/{id}/passengerGotOff')
