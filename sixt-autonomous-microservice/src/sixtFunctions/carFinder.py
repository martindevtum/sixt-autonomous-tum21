import json
import googlemaps as gmaps
from datetime import datetime

import apiInterfaces.sixtRequests.bookings as bookings
import apiInterfaces.sixtRequests.vehicles as vehicles

def find_best_cars(pickup_point):
    now = datetime.now()

    cars = vehicles.get_all()

    distance_results = []

    with open('config.json') as f:
        gmaps_client = gmaps.Client(key=json.load(f).get("api_key"))


    for i in range(0, len(cars), 25):
        cars_subset = cars[i:i+25]
        now = datetime.now()

        if cars_subset:
            car_pos = list(map(formatLatLon, cars_subset))
            result_gmaps = gmaps.distance_matrix.distance_matrix(gmaps_client, car_pos, pickup_point, "driving", departure_time=now)

            distances = to_distances(result_gmaps)

            distance_results = distance_results + list(map(lambda x, y: Merge(x, y), cars_subset, distances))
        else:
            break

    distance_results = list(filter(lambda x: check_availability(x) & check_charge(x), distance_results))
    list.sort(distance_results, key=lambda x: x['duration'])

    for x in distance_results:
        print(x)

    return distance_results

def check_availability(car):
    return car['status'] == 'FREE'

def check_charge(car, distance_to_customer_dest=0):
    PERCENT_PER_M = 100/550000
    RESERVE = 10

    needed_charge = (car['distance'] + distance_to_customer_dest) * PERCENT_PER_M + RESERVE

    return needed_charge <= float(car['charge'])

def formatLatLon(car):
    return f'{car.get("lat")},{car.get("lng")}'

def to_distances(result_gmaps):
    r = map(lambda x: x['elements'][0], result_gmaps['rows'])

    return map(lambda x: {
        'distance': x.get('distance', {'value' : 9999999999})['value'],
        'duration': x.get('duration_in_traffic', {'value' : 9999999999})['value']
    }, r)

# Python code to merge dict using update() method
def Merge(dict1, dict2):
    return {**dict1, **dict2}
