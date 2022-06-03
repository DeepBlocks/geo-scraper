### Parameters: modify these variables to fit your purpose ###

# path will be different for everyone depending on where this script is located
# most likely C:/Users/[USERNAME]/Downloads/[city_state] for Windows users
# or ~/Downloads/[city_state] for Mac users
path = "/mnt/g/.shortcut-targets-by-id/1CkRPe_N3e73wuPKr6tl12-tzk-yT4IkB/13 2022 Summer Internship/GIS Data/long_beach_ca/"

url = "https://services6.arcgis.com/yCArG7wGXGyWLqav/arcgis/rest/services/"

### Warning: Do not modify anything below this line unless you know what you are doing! ###

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import os

def loadPage(url):
    #print(url)
    req = Request(url)
    html_page = urlopen(req)
    return BeautifulSoup(html_page, "lxml")

def findLinks(url, searched, depth):
    if depth <= 0:
        return {}
    
    searched.append(url)
    soup = loadPage(url)
    
    links = {}
    for link in soup.findAll('a'):
        href = link.get('href')
        name = link.get_text()
        if not href.startswith('https://'):
            href = domain + href
        #print(searched)
        if 'FeatureServer' in href or 'MapServer' in href:
            if name not in links.keys() or 'MapServer' in links[name]:
                links[name] = href
                searched.append(href)
        elif ('services/' in href) and ('?' not in href) and (
            href not in searched) and (href != url):
            searched.append(href)
            links.update(findLinks(href, searched, depth - 1))
    
    return links

domain = url[:url.find('/', 8)]

links = findLinks(url, [], 3)

#print(links)

loadErrors = []
unicodeErrors = []

for page in links.keys():
    loaded = False
    
    index = page.rfind('/')
    newPath = page[:index + 1]
    pageName = page[index + 1:]
    
    if not os.path.exists(path + newPath):
        os.makedirs(path + newPath)
    
    geoURL = links[page] + "/0/query?outFields=*&where=1%3D1&f=geojson"
    print(geoURL)
    soup = None
    try:
        soup = loadPage(geoURL)
        loaded = True
    except:
        print("Failed to load " + page)
        loadErrors.append(page)
    if loaded == True:
        out = open(path + page + ".gjson", "w")
        try:
            out.write(soup.get_text())
        except UnicodeEncodeError:
            print("Failed to write to file " + page + ".gjson. Try downloading the file manually.")
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