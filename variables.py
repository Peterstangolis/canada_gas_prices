# a python file that contains variables used throughout the project for easy access - modification


# variables
oil_ticker = "CL=F"
cad_usd_ticker = "USDCAD=X"
period_1d = '1d'
period_last_month = '60d'
period_1y = '02y'
period_5y = '06y'
period_10y = '11y'
period_15y = '16y'
periods = (period_1d, period_last_month, period_1y, period_5y, period_10y, period_15y)

days = [1, 60]
years = [1, 5, 10, 15]


url_gaswizard = 'https://gaswizard.ca/gas-price-predictions/'

url_statscan = 'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000101&pickMembers%5B0%5D=2.2&cubeTimeFrame.startMonth=05&cubeTimeFrame.startYear=2022&cubeTimeFrame.endMonth=09&cubeTimeFrame.endYear=2022&referencePeriods=20220501%2C20220901'

Provinces = ["Ontario", "Quebec", "British Columbia", "Alberta", "Ontario", "Ontario", "PEI", "Ontario", "Alberta",
            "New Brunswick", "Ontario", "Nova Scotia", "Ontario", "British Columbia", "British Columbia", "Ontario", "Ontario",
            "Ontario", "Ontario", "Nova Scotia", "Ontario", "Ontario", "Ontario", "Ontario", "Ontario", "British Columbia",
            "Quebec", "Saskatchewan", "Saskatchewan", "Ontario", "New Brunswick", "Newfoundland & Labrador", "Ontario", "Ontario",
            "British Columbia", "Ontario", "Ontario", "Manitoba"]


flags = {'Ontario' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Flag_of_Ontario.svg/1920px-Flag_of_Ontario.svg.png',
        'Quebec' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/1280px-Flag_of_Quebec.svg.png',
        'Manitoba' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Flag_of_Manitoba.svg/1920px-Flag_of_Manitoba.svg.png',
        'Saskatchewan' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Flag_of_Saskatchewan.svg/1920px-Flag_of_Saskatchewan.svg.png',
        'PEI' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Flag_of_Prince_Edward_Island.svg/1280px-Flag_of_Prince_Edward_Island.svg.png',
        'New Brunswick' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Flag_of_New_Brunswick.svg/1920px-Flag_of_New_Brunswick.svg.png',
        'Nova Scotia' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Nova_Scotia_flag.svg/1920px-Nova_Scotia_flag.svg.png',
        'Newfoundland & Labrador' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Flag_of_Newfoundland_and_Labrador.svg/1920px-Flag_of_Newfoundland_and_Labrador.svg.png',
        'Alberta' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Flag_of_Alberta.svg/1920px-Flag_of_Alberta.svg.png',
        'British Columbia': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Flag_of_British_Columbia.svg/1920px-Flag_of_British_Columbia.svg.png'}

map_styles = {'basemap': ['https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}{r}.png',
                          'Tiles &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'],

              'NatGeoWorldMap': [
                  'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}',
                  'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC'],

              'EsriDeLorme': [
                  'https://server.arcgisonline.com/ArcGIS/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}',
                  'Tiles &copy; Esri &mdash; Copyright: &copy;2012 DeLorme'],

              'WorldTopoMap': ['https://{s}.tile.jawg.io/jawg-sunny/{z}/{x}/{y}{r}.png?access-token={accessToken}',
                               '<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'],

              'StamenTonerLite': ['https://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}{r}.png',
                                  'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors']
              }