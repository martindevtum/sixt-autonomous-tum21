import json

with open('./src/requests/mapsRequests/creds.json') as f:
    accessKey = json.load(f).get("api_key")

print(accessKey)
