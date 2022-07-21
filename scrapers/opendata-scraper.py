# Parameters: modify these variables to fit your purpose

# Path is likely C:/Users/[Username]/Downloads/[city_state]/ for Windows
# or ~/Downloads/[city_state]/ for Mac
print('Name of city (city_st):')
path = input() + '/'

print('Domain:')
domain = input()

# Warning: Do not modify anything below this line unless you know what you are doing!

import json
import requests
import os

os.chdir(os.path.dirname(__file__))

if not os.path.exists(path):
        os.makedirs(path)

url = "http://api.us.socrata.com/api/catalog/v1?domains=" + domain + "&search_context=" \
    + domain + "&only=maps"
print(url)

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
    
    r = requests.get(fileURL, timeout=300)
    if len(r.content) > 53:
        print(name)
        with open(path + fileName, 'wb') as f:
                f.write(r.content)

print("Done! Press Enter to continue...")
input()