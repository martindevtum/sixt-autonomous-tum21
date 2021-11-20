import requests.sixtRequests.bookings as bookings
import requests.sixtRequests.vehicles as vehicles

def setVehicleForBooking(booking):
  #calculate distance user to available cars
  costumerPickUp = [booking.pickupLat, booking.pickupLng]
  costumerDestination = [booking.destinationLat, booking.destinationLng]
  travelDist = getDistanceInKm(costumerPickUp, costumerDestination)

  distanceToCars = []
  allVehicles = bookings.getAllVehicles()

  for vehicle in allVehicles:
    vId = vehicle.get('id')
    for coord in vehicles.getVehicleLocationById(vId):
      latVehicle = coord.get('lat')
      lngVehicle = coord.get('lng')


def getDistanceInKm(pickUp, destination):
