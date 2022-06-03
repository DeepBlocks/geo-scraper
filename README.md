# RE Deepblocks 2022
## Arcgis Scraper
The arcgis scraper should work for most websites that run on arcgis.

### Instructions
1. Download arcgis-scraper.py
2. Open any website that uses arcgis
    - Note: not all arcgis sites say arcgis in the URL
3. Click on the search bar and then click "Data"
![Screenshot of searchbar](/assets/images/search.png)
4. Click on any of the results, then click on "I want to use this" in the bottom left corner once the map shows up
![Screenshot of the "I want to use this" button](/assets/images/i-want-to-use-this.png)
5. Click on "View API Resources," then click on the "View" button next to GeoJSON
![](/assets/images/view-api-resources.png)
6. In the URL bar, delete everything after "services/" (Highlighted in blue below)
![](/assets/images/URL-bar.png)
7. Open the program you downloaded with any text editor (DO NOT DOUBLE CLICK THE PROGRAM)
    - Windows: Right click the program, then hover over "Open with" and click Notepad
    - Mac: Right click the program, then hover over "Open with" and click TextEdit
8. Change `url` to the new URL you just got (make sure to keep the quotation marks)
9. Change `path` to fit your needs
10. Open command prompt (if on Windows) or terminal (if on Mac)
11. Type `cd Downloads/`
12. Type `python arcgis-scraper.py`
13. Copy the new folder into the shared Google Drive