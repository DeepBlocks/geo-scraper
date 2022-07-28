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
6. Download arcgis-scraper.py from releases and run it
![](/assets/images/releases.png)
7. Input the city name and the URL when asked
    - Input the city name as city_st (e.g. las_vegas_nv)

## Opendata Scraper
The opendata scraper should work for most websites that use the Open Data Network (typically the URL would start with data e.g. [data.oaklandca.gov](https://data.oaklandca.gov/))

### Instructions
1. Download opendata-scraper.py from releases
![](/assets/images/releases.png)
2. Copy the URL excluding https:// and any slashes (i.e. only copy data.example.com, not https://data.example.com/pages)
3. Run the program and input the city name and URL when asked
    - Input the city name as city_st (e.g. las_vegas_nv)

## How to tell if a site is arcgis or opendata
Click on the search field. If the word "Data" appears underneath, then the site likely uses arcgis.
![](/assets/images/search.png)
This site uses arcgis because the word "Data" appears.
