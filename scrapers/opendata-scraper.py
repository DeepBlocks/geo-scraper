# Parameters: modify these variables to fit your purpose

domain = "data.cityofnewyork.us"
tags = ["doittgis", "doitt gis", "gis"]

# Path is likely C:/Users/[Username]/Downloads/[city_state]/ for Windows
# or ~/Downloads/[city_state]/ for Mac
path = "G:/.shortcut-targets-by-id/1CkRPe_N3e73wuPKr6tl12-tzk-yT4IkB/13 2022 Summer Internship/GIS Data/nyc_ny/"

# Warning: Do not modify anything below this line unless you know what you are doing!

import json
import requests
import os

if not os.path.exists(path):
        os.makedirs(path)

def formatTags(tags):
    ret = ""
    for tag in tags:
        ret += tag.replace(" ","%20") + "%2C"
    return ret[:len(ret) - 3]

url = "http://api.us.socrata.com/api/catalog/v1?domains=" + domain + "&search_context=" \
    + domain + "&tags=" + formatTags(tags)

data = requests.get(url).json()
for result in data["results"]:
    name = result["resource"]["name"]
    print(name)
    fileURL = "https://" + domain + "/api/geospatial/" + result["resource"]["id"] + "?method=export&format=GeoJSON"
    fileName = name + ".geojson"
    
    r = requests.get(fileURL)
    with open(path + fileName, 'wb') as f:
        f.write(r.content)

print("Done!")