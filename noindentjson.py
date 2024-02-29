import json

with open('data.json', 'r') as f:
    data_json = json.load(f)

with open('data.geojson', 'w') as outfile:
    json.dump(data_json, outfile, indent=None)