# RE Deepblocks 2022

## Contents
[Arcgis Scraper](/README.md#arcgis-scraper)

[Opendata Scraper](/README.md#opendata-scraper)

[How to tell if a site is arcgis or opendata](/README.md#how-to-tell-if-a-site-is-arcgis-or-opendata)

## Arcgis Scraper
The arcgis scraper should work for most websites that run on arcgis.

### Instructions
1. Open any website that uses arcgis
    - Note: not all arcgis sites say arcgis in the URL
2. Click on the search bar and then click "Data"
![Screenshot of searchbar](/assets/images/search.png)
3. Click on any of the results, then click on "I want to use this" in the bottom left corner once the map shows up
![Screenshot of the "I want to use this" button](/assets/images/i-want-to-use-this.png)
4. Click on "View Data Source," then click on the "View" button next to GeoJSON
![](/assets/images/view-storage.png)
5. At the top, click Home and copy the URL
6. Download arcgis-scraper.py from Releases and open it with a text editor (DO NOT JUST CLICK OR DOUBLE CLICK ON IT)
    - Windows: Right click the program, then hover over "Open with" and click Notepad
    - Mac: Right click the program, then hover over "Open with" and click TextEdit
![](/assets/images/releases.png)
7. Change `url` to the new URL you just got (make sure to keep the quotation marks and the / after `services`)
8. Change `path` to fit your needs
9. Open command prompt (if on Windows) or terminal (if on Mac)
10. Type `cd Downloads/`
11. Type `python arcgis-scraper.py` and wait for the program to output `Done!`
12. Copy the new folder into the shared Google Drive
13. If there is an error message, copy the error messages, double click the "Notes" column in the Google Sheets, and paste the error message

## Opendata Scraper
The opendata scraper should work for most websites that use the Open Data Network (typically the URL would start with data e.g. [data.oaklandca.gov](https://data.oaklandca.gov/))

### Instructions
1. Download opendata-scraper.py from Releases and open it with a text editor (DO NOT JUST CLICK OR DOUBLE CLICK ON IT)
    - Windows: Right click the program, then hover over "Open with" and click Notepad
    - Mac: Right click the program, then hover over "Open with" and click TextEdit
![](/assets/images/releases.png)
2. Copy the URL excluding https:// and any slashes (i.e. only copy data.example.com, not https://data.example.com/pages)
3. In the code, change `domain` to the URL you copied
4. Change `path` to your path
5. Open command prompt (if on Windows) or terminal (if on Mac)
6. Type `cd Downloads/`
7. Type `python opendata-scraper.py`
8. Copy the new folder into the shared Google Drive

## How to tell if a site is arcgis or opendata
Click on the search field. If the word "Data" appears underneath, then the site likely uses arcgis.
![](/assets/images/search.png)
This site uses arcgis because the word "Data" appears.
