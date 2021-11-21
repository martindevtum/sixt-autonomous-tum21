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

    return distance_results

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
