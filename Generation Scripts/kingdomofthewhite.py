
import folium
from folium.plugins import MeasureControl, MousePosition, MiniMap
from pathlib import Path
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.interpolate import griddata
import geojsoncontour
import numpy as np
import scipy as sp
import scipy.ndimage
import branca



white_url = Path('../Kingdom of the White Map/Kingdom Of the WhiteScaled.png')
white_url2 = Path('../Kingdom of the White Map/Kingdom Of the White.png')
# Create a map centered at a specific location
tile_url = Path('./Kingdom of the White Map/tiles/{z}/{x}/{-y}.png')
tile_url2 = Path('./World Map/tileshires/{z}/{x}/{-y}.png')
# Create a map centered at a specific location
m = folium.Map(location=[70, -90], zoom_start=6, min_zoom=6, max_zoom=10,control_scale = True,tiles=None)
folium.TileLayer(tiles=tile_url.as_posix(),attr='Russell',crs='EPSG3857', name='Kingdom of the White',zoom_start=6, min_zoom=6, max_zoom=10,).add_to(m)
folium.TileLayer(tiles=tile_url2.as_posix(),attr='Russell',crs='EPSG3857', name='World Map',zoom_start=6, min_zoom=6, max_zoom=10,).add_to(m)



formatter = "function(num) {return L.Util.formatNum(num, 5) + ' º ';};"
#MeasureControl().add_to(m)
folium.plugins.MousePosition(
    position="topright",
    separator=" | ",
    empty_string="NaN",
    lng_first=True,
    num_digits=20,
    prefix="Coordinates:",
    lat_formatter=formatter,
    lng_formatter=formatter,
).add_to(m)

import geopandas as gpd

from shapely.geometry import Polygon, Point, LineString
import pandas as pd

HiddenValley=pd.read_csv(Path(
    "HiddenValley.csv").as_posix())
boundarypoints=[]
for item in range(len(HiddenValley['Lat'])):
    boundarypoints.append([HiddenValley['Lat'][item],HiddenValley['Lon'][item]])
HiddenValleyBoundary = Polygon(boundarypoints)
WhiteRegions = gpd.GeoDataFrame(index=[0], crs="EPSG:4326", geometry=[HiddenValleyBoundary])
WhiteRegions["Territory"]=['The Hidden Valley']
WhiteRegions["RGBA"]=[[11, 127, 171, 1]]
data = pd.DataFrame({
   'lon':[-90.04669,-90.5287,-89.86954],
   'lat':[71.00087,70.01167,69.86375],
   'name':['Dragon Roost (HQ) <br> 7 Knights <br> 3 Archers','Bandit Broch (Ruined)','Storm Castle <br> 21 Knights <br> 3 Archers <br> Zepplin Crew <br> Medical Crew']
}, dtype=str)
neutral=pd.DataFrame({
    'lon':[-91.27441,-89.37927,-88.49487,-87.45117,-86.82495,-87.08313,-86.77551,-87.5116,-87.96553,-88.57178,-89.42322,-87.09961,-91.38977,-89.48914,-88.26965,-87.57202,-89.2197,-89.599,-89.77478,-90.53833,-91.42822,-90.30762],
    'lat':[71.03928,71.44642,71.43767,71.68772,71.8682,70.79775,70.73804,70.69087,71.02053,70.86449,70.95611,71.37286,70.76882,70.75253,71.36409,71.83398,71.64637,71.61348,71.39916,71.34477,71.64464,72.25227],
    'name':['Western Tower','Milky Lake','Waterfall Hamlet','Forest Hamlet','Mine Hamlet','Town of White Tooth','Icetooth Bay','Forest Bridge','Rainbow Bridge','Gold Mine','White River','Dark Forest','Western Forest','Misty Valley','Pastel River','Dragon Roost','Dragon Roost','Dragon Roost','Dragon Roost','Dragon Roost','Dragon Roost','Dragon Roost?']
},dtype=str)
enemies=pd.DataFrame({
    'lon':[-89.65942,-89.41223],
    'lat':[70.27892,70.27492],
    'name':['Western Bullwark <br> (Internal Security','Last Refuge <br> (Penal Battalion)']
},dtype=str)
for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
      tooltip=data.iloc[i]['name'],
      icon=folium.Icon(color='darkred',icon='glyphicon-flag')
   ).add_to(m)

for i in range(0,len(neutral)):
   folium.Marker(
      location=[neutral.iloc[i]['lat'], neutral.iloc[i]['lon']],
      popup=neutral.iloc[i]['name'],
      tooltip=neutral.iloc[i]['name'],
      icon=folium.Icon(color='lightgray',icon='glyphicon-flag')
   ).add_to(m)

for i in range(0,len(enemies)):
   folium.Marker(
      location=[enemies.iloc[i]['lat'], enemies.iloc[i]['lon']],
      popup=enemies.iloc[i]['name'],
      tooltip=enemies.iloc[i]['name'],
      icon=folium.Icon(color='orange',icon='glyphicon-flag')
   ).add_to(m)

folium.Marker(
    location=[71.87845, -88.75305],
    popup="Von Gefroren's Castle <br> (Over Wintering)",
    tooltip="Von Gefroren's Castle <br> (Over Wintering)",
    icon=folium.Icon(color='darkblue',icon='glyphicon-flag')
   ).add_to(m)
#Time Stamped GeoJson
from io import BytesIO
import base64

png = "./RenderedRedFortune.png"
with open(png, "rb") as lf:
    # open in binary mode, read bytes, encode, decode obtained bytes as utf-8 string
    red_fortune_icon = base64.b64encode(lf.read()).decode("utf-8")
geo_features = list()
geo_json = {
    "type": "FeatureCollection",
    "features": geo_features,
}
folium.GeoJson(WhiteRegions.__geo_interface__,
               name="Kingdom of the White Regions",
               style_function=lambda feature: {'fillColor': feature['properties']['RGBA'],
                                               #'color' : feature['properties']['RGBA'],
                                               'weight' : 1,
                                               'fillOpacity' : 0.5},
               tooltip=folium.features.GeoJsonTooltip(["Territory"])
               ).add_to(m)

CampaignPath=gpd.GeoDataFrame({
    'Flight of the Red Fortune':['Flight Path'],
    'geometry':[LineString([(71.00087,-90.04669),(70.01167,-90.5287),(69.86375,-89.86954)])]},
    crs="EPSG:4326")


folium.LayerControl().add_to(m)
# Display the map
m.save("../KingdomoftheWhite.html")
