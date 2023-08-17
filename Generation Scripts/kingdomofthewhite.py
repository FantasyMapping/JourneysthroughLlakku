
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


folium.LayerControl().add_to(m)
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
from shapely.geometry import Polygon
import pandas as pd
data = pd.DataFrame({
   'lon':[-90.04669,-90.5287,-89.86954],
   'lat':[71.00087,70.01167,69.86375],
   'name':['Dragon Roost (Initial Base)','Bandit Broch (Ruined)','Storm Castle']
}, dtype=str)

for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
      icon=folium.Icon(color='darkred',icon='glyphicon-flag')
   ).add_to(m)

folium.Marker(
    location=[71.87845, -88.75305],
    popup="Von Gefroren's Castle \n (Over Wintering)",
    icon=folium.Icon(color='darkblue',icon='glyphicon-flag')
   ).add_to(m)
# Display the map
m.save("../KingdomoftheWhite.html")
