### Parameters: modify these variables to fit your purpose ###

# path will be different for everyone depending on where this script is located
# most likely C:/Users/[USERNAME]/Downloads/[city_state]/ for Windows users
# or ~/Downloads/[city_state]/ for Mac users
path = "G:/.shortcut-targets-by-id/1CkRPe_N3e73wuPKr6tl12-tzk-yT4IkB/13 2022 Summer Internship/GIS Data/philadelphia_pa/"

# Make sure to include the / after services
url = "https://services.arcgis.com/fLeGjb7u4uXqeF9q/ArcGIS/rest/services"

### Warning: Do not modify anything below this line unless you know what you are doing! ###

from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
import re
import os
from os.path import exists
import csv

from requests import RequestException

links = {}

def loadPage(url):
    #print(url)
    req = Request(url)
    try:
        html_page = urlopen(req)
    except urllib.error.URLError:
        raise urllib.error.URLError('Failed to load ' + url)
    return BeautifulSoup(html_page, "lxml")

def findLinks(url, searched, depth):
    if depth <= 0:
        return {}
    
    searched.append(url)
    soup = loadPage(url)
    
    for link in soup.findAll('a'):
        href = link.get('href')
        name = link.get_text().strip()
        if not href.startswith('https://') and not href.startswith('http://'):
            href = domain + href
        #print(searched)
        if 'FeatureServer' in href or 'MapServer' in href:
            links.update(getLayers(href, name + '/'))
            searched.append(href)
        elif ('services/' in href) and (href not in searched) and (href != url) and href.startswith(domain):
            searched.append(href)
            findLinks(href, searched, depth - 1)

def getLayers(url, path):
    soup = loadPage(url)
    for link in soup.findAll('a'):
        href = link.get('href')
        endIndex = 0
        if '?' in href:
            endIndex = href.find('?')
        else:
            endIndex = len(href)
        if href[href.rfind('Server/') + 7:endIndex].isnumeric():
            name = path + link.get_text().strip().replace('/','%2F')
            if name not in links.keys() or 'MapServer' in links[name]:
                if not href.startswith('https://'):
                    href = domain + href
                links[name] = href
                print(name)
    return links
    
def cleanName(name):
    name = name.replace('<', "%3C")
    name = name.replace('>', "%3E")
    name = name.replace(':', "%3A")
    name = name.replace('"', "%22")
    name = name.replace('|', "%7C")
    name = name.replace('?', "%3F")
    name = name.replace('*', "%2A")
    return name


# Main Program

domain = url[:url.find('/', 8)]
if not os.path.exists(path):
        os.makedirs(path)

print("Scanning for links...")
if not exists(path + "links.csv"):
    findLinks(url, [], 4)
    f = open(path + 'links.csv', 'w')
    f.write("name,href\n")
    for entry in links.keys():
        f.write('"' + entry + '",' + links[entry] + "\n")
    f.close()
else:
    with open(path + "links.csv", 'r', encoding="utf8") as f:
        csv_reader = csv.DictReader(f)
        #next(csv_reader)
        for line in csv_reader:
            links[line['name']] = line['href']



loadErrors = []
unicodeErrors = []

print("Downloading data...")
for page in links.keys():
    loaded = False
    
    index = page.rfind('/')
    newPath = cleanName(page[:index + 1])
    
    if not os.path.exists(path + newPath):
        os.makedirs(path + newPath)
    
    if not exists(path + cleanName(page) + ".geojson"):
        geoURL = links[page] + "/query?outFields=*&where=1%3D1&f=geojson"
        print(geoURL)
        soup = None
        try:
            soup = loadPage(geoURL)
            loaded = True
        except:
            print("Failed to load " + page)
            loadErrors.append(page)
        if loaded == True:
            out = open(path + cleanName(page) + ".geojson", "w")
            try:
                out.write(soup.get_text())
            except UnicodeEncodeError:
                print("Failed to write to file " + page + ".geojson. Try downloading the file manually.")
                unicodeErrors.append(page)
            out.close()
        
print("Done! Paste any errors in the Notes section of the spreadsheet.")
if len(loadErrors) > 0:
    print("Load Errors:")
    for item in loadErrors:
        print(" - " + item)
if len(unicodeErrors) > 0:
    print("Unicode Errors:")
    for item in unicodeErrors:
        print(" - " + item)