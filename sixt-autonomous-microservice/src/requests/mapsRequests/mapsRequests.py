import json
import requests
import time

API_ENDPOINT = 'https://maps.googleapis.com/maps/api/distancematrix/json'

with open('./src/requests/creds.json') as f:
    accessKey = json.load(f).get("api_key")

"""
start: (lat, lon)
dest: (lat, lon)

returns: (distance in m, duration in s)
"""

def getPathData(start, dest):
    params = {
        'origins': f'{start[0]},{start[1]}',
        'destinations': f'{dest[0]},{dest[1]}',
        'driving': 'driving',
        'departure_time': int(time.time()),
        'key': accessKey
    }

    r = requests.get(API_ENDPOINT, params=params)
    firstRoute = json.loads(r.text)['rows'][0]['elements'][0]

    return (firstRoute['distance']['value'], firstRoute['duration_in_traffic']['value'])


if __name__ == "__main__":
    print(getPathData((48.158055,11.544692), (48.166420, 11.590755)))
