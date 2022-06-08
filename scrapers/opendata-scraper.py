# Parameters: modify these variables to fit your purpose

domain = "data.buffalony.gov"

# Path is likely C:/Users/[Username]/Downloads/[city_state]/ for Windows
# or ~/Downloads/[city_state]/ for Mac
path = "G:/.shortcut-targets-by-id/1CkRPe_N3e73wuPKr6tl12-tzk-yT4IkB/13 2022 Summer Internship/GIS Data/buffalo_ny/"

# Warning: Do not modify anything below this line unless you know what you are doing!

import json
import requests
import os

if not os.path.exists(path):
        os.makedirs(path)

url = "http://api.us.socrata.com/api/catalog/v1?domains=" + domain + "&search_context=" \
    + domain + "&only=maps"

def cleanName(name):
    name = name.replace('<', "%3C")
    name = name.replace('>', "%3E")
    name = name.replace(':', "%3A")
    name = name.replace('"', "%22")
    name = name.replace('|', "%7C")
    name = name.replace('?', "%3F")
    name = name.replace('*', "%2A")
    name = name.replace('/','%2F')
    return name

data = requests.get(url).json()
for result in data["results"]:
    name = result["resource"]["name"]
    fileURL = "https://" + domain + "/api/geospatial/" + result["resource"]["id"] + "?method=export&format=GeoJSON"
    fileName = cleanName(name) + ".geojson"
    
    if not exists(path + fileName):
        r = requests.get(fileURL)
        if len(r.content) > 53:
            print(name)
            with open(path + fileName, 'wb') as f:
                    f.write(r.content)
            f.close()

print("Done!")
