import json

with open('./src/requests/creds.json') as f:
    accessKey = json.load(f).get("api_key")

print(accessKey)
