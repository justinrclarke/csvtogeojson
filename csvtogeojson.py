import csv
from geojson import Feature, FeatureCollection, Point

features = []
with open('data.csv', newline='') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    
    # Skip first line of the CSV, as it is the header.
    next(reader)
    
    for column_1, column_2, column_3, column_4, column_5 in reader:
        latitude = float(column_2)
        longitude = float(column_3)
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'count': int(column_3)
                }
            )
        )

collection = FeatureCollection(features)
with open("data.geojson", "w") as f:
    f.write('%s' % collection)
