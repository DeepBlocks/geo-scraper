# RE Deepblocks 2022
## Arcgis Scraper
The arcgis scraper should work for most websites that run on arcgis.

### Instructions
1. Open any website that uses arcgis
    - Note: not all arcgis sites say arcgis in the URL
2. Click on the search bar and then click "Data"
![Screenshot of searchbar](/assets/images/search.png)
3. Click on any of the results, then click on "I want to use this" in the bottom left corner once the map shows up
![Screenshot of the "I want to use this" button](/assets/images/i-want-to-use-this.png)
4. Click on "View API Resources," then click on the "View" button next to GeoJSON
![](/assets/images/view-api-resources.png)
5. In the URL bar, delete everything after "services/" (Highlighted in blue below)
![](/assets/images/URL-bar.png)
6. Download arcgis-scraper.py and open it with a text editor (DO NOT JUST CLICK OR DOUBLE CLICK ON IT)
    - Windows: Right click the program, then hover over "Open with" and click Notepad
    - Mac: Right click the program, then hover over "Open with" and click TextEdit
7. Change `url` to the new URL you just got (make sure to keep the quotation marks)
8. Change `path` to fit your needs
9. Open command prompt (if on Windows) or terminal (if on Mac)
10. Type `cd Downloads/`
11. Type `python arcgis-scraper.py`
12. Copy the new folder into the shared Google Drive
