import json

with open('creds.json') as f:
    accessKey = json.load(f).get("api_key")

print(accessKey)
