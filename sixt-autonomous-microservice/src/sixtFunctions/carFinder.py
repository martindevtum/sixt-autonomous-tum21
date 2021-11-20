import googlemaps as gmaps
from datetime import datetime

import requests.sixtRequests.bookings as bookings
import requests.sixtRequests.vehicles as vehicles

def find_best_car(pickup_point):
    now = datetime.now()

    cars = vehicles.get_all()

    for i in range(0,len(cars),25):
        cars_subset = cars[i:i+25]
        if cars_subset:
            for car in cars_subset:
                print(car)
        else:
            break
