# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:16:14 2023

@author: lycea
"""

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



tile_url = Path('./World Map/tileshires/{z}/{x}/{-y}.png')
# Create a map centered at a specific location
m = folium.Map(location=[40.7128, -74.0060], zoom_start=3, min_zoom=2, max_zoom=8, tiles=tile_url.as_posix(),control_scale = True,attr='World Map',crs='EPSG3857', name='World Map')



# rawimage=Path("C:/Users/lycea/Documents/40-49 Personal/48 Gaming/48.04 Greyhawk Campaign/World Map/Altitude 1 Tile/A000000.raw")
# test=open(rawimage.as_posix(),'rb')
# img = np.fromfile(test, dtype=np.float32,count=16000*32000).reshape(16000,32000)
# longitude_per_pixel=360/img.shape[1]
# latitude_per_pixel=180/img.shape[0]
# latitudes=np.linspace(-90,90,img.shape[0])
# longitudes=np.linspace(-180,180,img.shape[1])
# lat_mesh,lon_mesh=np.meshgrid(longitudes,latitudes)
# #z_mesh=griddata((latitudes,longitudes),img,(lat_mesh,lon_mesh),method='linear')
# contour_interval=250
# steps=np.linspace(np.floor(np.min(img)/contour_interval)*contour_interval,np.ceil(np.max(img)/contour_interval)*contour_interval,int(np.ceil(np.max(img)/contour_interval)-np.floor(np.min(img)/contour_interval)+1))
# # Setup minimum and maximum values for the contour lines
# vmin = steps.min() 
# vmax = steps.max()# Setup colormap
# #colors = ['blue','royalblue', 'navy','pink',  'mediumpurple',  'darkorchid',  'plum',  'm', 'mediumvioletred', 'palevioletred', 'crimson',
# #         'magenta','pink','red','yellow','orange', 'brown','green', 'darkgreen']
# colors=['blue','yellow']
# #levels = len(colors)
#cm     = branca.colormap.LinearColormap(colors, vmin=vmin, vmax=vmax).to_step(levels)

#import branca.colormap as cmp
#cm = branca.colormap.LinearColormap(
#    ['blue','yellow'],
#    vmin=vmin, vmax=vmax,
#    caption='Color Scale for Map' #Caption for Color scale or Legend
#).to_step(len(steps))

# Use Gaussian filter to smoothen the contour
#sigma = [5, 5]
#z_mesh = sp.ndimage.filters.gaussian_filter(z_mesh, sigma, mode='constant')
# Create the contour
#contourf = plt.contourf(lat_mesh, lon_mesh,img, steps, alpha=0.5, colors=colors, linestyles='None', vmin=vmin, vmax=vmax)
# Convert matplotlib contourf to geojson
#geojson = geojsoncontour.contourf_to_geojson(
#    contourf=contourf,
#    min_angle_deg=3.0,
#    ndigits=5,
#    stroke_width=0.2,
#    fill_opacity=0.25)

# Plot the contour on Folium map
#folium.GeoJson(
#    geojson,
#    style_function=lambda x: {
#        'color':     x['properties']['stroke'],
#        'weight':    x['properties']['stroke-width'],
#        'fillColor': x['properties']['fill'],
#        'opacity':   0.5,
#    }).add_to(m)
#import map tiles

#tile_layer = folium.TileLayer(tile_url, opacity=1, attr='My Tile Layer', name='My Tile Layer')
#tile_layer.add_to(m)


from folium.features import DivIcon
#folium.Marker(p1, icon=DivIcon(
#        icon_size=(150,36),
#        icon_anchor=(7,20),
#        html='<div style="font-size: 18pt; color : black">1</div>',
#        )).add_to(m)
#m.add_child(folium.CircleMarker(p1, radius=15))
# Define the path to the image file
#image_path = '../../../Documents/40-49 Personal/48 Gaming/48.04 Greyhawk Campaign/RailMap2.png'

# Define the boundaries of the image
#image_bounds = [[60, -30.0060], [10, -130]]
#political_countries_url = (

#    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"

#)
#add contours
#field_locations=Path("C:/Users/lycea/Documents/40-49 Personal/48 Gaming/48.04 Greyhawk Campaign/World Map/altitudecontours.geojson")
#folium.GeoJson(field_locations.as_posix()
#              ).add_to(m)

#folium.GeoJson(political_countries_url,name="Greyhawk Tunnel Map").add_to(m)
# Add the image overlay to the map
#folium.raster_layers.ImageOverlay(image_path,name="Greyhawk Tunnel Map", bounds=image_bounds).add_to(m)
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
# Create a feature group to hold the ship's marker
ship_fg = folium.FeatureGroup(name='Fortuna Rubrum')

#ship icon
# Create a list of coordinates for the ship's journey
coordinates = [[40.7128, -74.0060], [41.8781, -87.6298], [37.7749, -122.4194]]
current_location=[71.13099,-91.23047]
redfortune_url=Path('./RenderedRedFortune.png')
#icon = folium.features.CustomIcon(redfortune_url.as_posix(),
#                                      icon_size=(64,64))

#redfortune_static=folium.Marker(current_location,icon=icon).add_to(m)

import geopandas as gpd
from shapely.geometry import Polygon
import pandas as pd
data = pd.DataFrame({
   'lon':[-103.35938, -93.66943, -99.06205, -69.16992,-9.7229,-95.58105,-105.0293,-71.80664,-92.30164,-89.67041,-88.72559,-106.25977,-63.94643,-54.97559,-68.6865,-66.44531,-60.11719,-59.50195,-53.34961,-89.64844,-99.31641,30.19043,-95.27344,-101.57959,-114.16992,-120.844961,-106.08398,-100.19531,-61.45752,-72.99316],
   'lat':[10.31492, 26.64746, 29.45873, 50.40152,5.40821,51.5634,62.34961,60.19616,26.77994,46.30006,48.3416,45.22074,51.08282,45.6294,58.11852,59.1159,49.21042,55.22902,47.29413,40.58058,58.53959,19.72534,48.10743,-5.41915,5.09094,2.72338,-8.14624,11.69527,51.72703,47.87214],
   'name':['Llewllaff', "Y'Bent", 'Golden Helm', 'Pears','Griffin Peak','Seventh Star','Reich','Ruins of Graecity (Underground)?','Fish Bay (Underground)?','The University (Underground)?', 'Southton (Underground)?','The Holy City','Iron City (Underground)?','The Devoted','Nyr Dyvn Greatlake (Underground)?','East Fort','Tall Town','Calm Bay (Underground)?','Beachview (Underground)?','Hotsprings (Underground)?','West Fort','City of the God King','Dipolmat (Underground)?','Pirate Kings','Roaring Heights (Underground)?','Botanical Bridge (Underground)?','Southern Port (Underground)?','Llewllaff (Underground)','Mining Town','Southern Confluence?']
}, dtype=str)

CityData=pd.read_csv(Path("LlakkuCity.csv").as_posix())

#Territory Colors
style1 = {'fillColor': '#228B22', 'color': '#228B22'}
style2 = {'fillColor': '#00FFFFFF', 'color': '#00FFFFFF'}

GriffinPeakTerritory=pd.read_csv(Path(
    "GriffinPeakCommonwealth.csv").as_posix())
ReichTerritory=pd.read_csv(Path(
    "Reich.csv").as_posix())
TheLittleKingdoms=pd.read_csv(Path(
    "TheLittleKingdoms.csv").as_posix())
boundarypoints=[]
for item in range(len(GriffinPeakTerritory['Lat'])):
    boundarypoints.append([GriffinPeakTerritory['Lat'][item],GriffinPeakTerritory['Lon'][item]])
GriffinPeakBoundary = Polygon(boundarypoints)

boundarypoints=[]
for item in range(len(ReichTerritory['Lat'])):
    boundarypoints.append([ReichTerritory['Lat'][item],ReichTerritory['Lon'][item]])    
ReichBoundary = Polygon(boundarypoints)

boundarypoints=[]
for item in range(len(TheLittleKingdoms['Lat'])):
    boundarypoints.append([TheLittleKingdoms['Lat'][item],TheLittleKingdoms['Lon'][item]])
TheLittleKingdomsBoundary = Polygon(boundarypoints)

crs = {'init': 'epsg:4326'}
ClaimedTerritory = gpd.GeoDataFrame(index=[0,1,2], crs=crs, geometry=[GriffinPeakBoundary,
                                                                    ReichBoundary,
                                                                    TheLittleKingdomsBoundary])
ClaimedTerritory["Territory"]=['Griffin Peak Commonwealth','Reich','The Little Kingdoms']
ClaimedTerritory["RGBA"]=[[11, 127, 171, 1],[255, 76, 48, 1],[192,192,192,1]]


#Add Claimed Boundaries
#for key in ClaimedTerritory.iterrows():
#     footprint = key[1][0]
#     fillColor = key[1][2]
#     color = key[1][2]
#     feat = folium.GeoJson(
#         footprint,
#         style_function=lambda x, fillColor=fillColor, color=color: {
#             "fillColor": fillColor,
#             "color": color,
#         },
#         highlight_function=lambda feature: {"fillcolor": "green", "color": "green"},
#         name="National Boundaries",
#         tooltip=folium.features.GeoJsonTooltip(key[1][1])
#     )

#feat.add_to(m)
# style function from https://gis.stackexchange.com/questions/433810/folium-draw-and-highlight-polylines-with-distinct-colours-from-unique-geojson
roads_style_function = lambda x: {
  # specifying properties from GeoJSON
  'color' :   x['properties']['stroke'],
  'opacity' : 0.50,
  'weight' : x['properties']['stroke-width'],
  'dashArray' : x['properties']['dashArray']
}

# highlight function (change displayed on hover)
roads_highlight_function = lambda x: {
  'color' :   x['properties']['stroke'],
  'opacity' : 0.90,
  # specifying properties from GeoJSON
  'weight' : x['properties']['stroke-width'],
  'dashArray' : x['properties']['dashArray-highlight']
}

folium.GeoJson(ClaimedTerritory.__geo_interface__,
               name="National Boundaries",
               style_function=lambda feature: {'fillColor': feature['properties']['RGBA'],
                                               #'color' : feature['properties']['RGBA'],
                                               'weight' : 1,
                                               'fillOpacity' : 0.5},
               tooltip=folium.features.GeoJsonTooltip(["Territory"])
               ).add_to(m)

for i in range(0,len(CityData)):
   folium.Marker(
      location=[CityData.iloc[i]['Lat'], CityData.iloc[i]['Lon']],
      popup=CityData.iloc[i]['Name'],
   ).add_to(m)
   
# Llewllaff=[-103.35938,10.31492]
# YBent=[-93.66943,26.64746]
# GoldenHelm=[-99.60205,29.45873]
# Pears=[-69.03809,53.56641]
# Add the ship's marker to the feature group
folium.Marker(location=current_location, popup='Ship Location',tooltip='Fortuna Rubrum', icon=folium.features.CustomIcon(icon_image=redfortune_url.as_posix(), icon_size=(2*72, 2*50))).add_to(ship_fg)

# Add the ship's feature group to the map
m.add_child(ship_fg)

# Create a feature group to hold the ship's trajectory
#trajectory_fg = folium.FeatureGroup(name='Trajectory')

# Add the ship's trajectory to the feature group
#folium.PolyLine(locations=coordinates, color='red', weight=3).add_to(trajectory_fg)

# Add the ship's trajectory feature group to the map
#m.add_child(trajectory_fg)

# Add a layer control to the map to toggle the ship and trajectory feature groups
folium.LayerControl().add_to(m)
#cm.caption = 'Elevation'
#m.add_child(cm)
#add minimap
#MiniMap(tile_layer=tile_url,attr='World Map').add_to(m)

# Display the map
m.save("../Llakku.html")