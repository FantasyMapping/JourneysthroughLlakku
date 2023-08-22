# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:10:51 2023

@author: lycea
"""

import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson
from pathlib import Path
import numpy as np

def bearing(position,next_position):
    diff=np.radians(next_position)-np.radians(position)
    angle=np.degrees((np.arctan2(diff[1],diff[0]))+0)% 360
    return angle

def rotated_ship(position,angle=0,
                   icon_size=(2*72,2*50),
                   tooltip_str='Fortuna Rubrum <br> Docked at Storm Castle <br> 21 Knights <br> 3 Archers <br> Zepplin Crew <br> Medical Crew',
                   popup_str='Ship Location'):

    rfindex=index_ship_headings(Path('./Airship Assets/Airship Headings/RenderedRedFortune00deg.png').parent)

    r_marker=folium.Marker(location=position,
                           popup=popup_str,
                           tooltip=tooltip_str,
                           #icon=folium.Icon(color='lightgray',icon='glyphicon-flag'),
                           icon=folium.features.CustomIcon(icon_image=rfindex[indexinground(angle)][0].as_posix(),
                                                           icon_size=icon_size),
                           angle=angle)


    return r_marker

def indexinground(x, base=10):
    return int(base * round(float(x)/base))

def index_ship_headings(parent):
    import re
    
    rfindex={}
    for file in parent.iterdir():
        if any(c.isdigit() for c in file.name):
            # get number
            number = int(re.findall(r'\d+', file.name)[0])
            if number not in rfindex:
                rfindex[number] = []
            rfindex[number].append(file)
            
    return rfindex

rfindex=index_ship_headings(Path('./Airship Assets/Airship Headings/RenderedRedFortune00deg.png').parent)


# Import the CSV file

point_list = pd.read_csv('FlightoftheRedFortune_WinterCampaign.csv',parse_dates=True, index_col='datetime')
#create time index
#point_list['datetime']=pd.date_range(start='2023-08-22 12:00:00',end='2023-08-29 12:00:00',periods=len(point_list))
#point_list.set_index('datetime',inplace=True)

fine_detail=point_list.resample('60min').interpolate(method='linear')
# Create a TimestampedGeoJSON object
#angle=0
coords=[]
for i in range(len(fine_detail)):
    coords.append([])
    for inc in range(i):
        coords[i].append([fine_detail['Lat'].iloc[inc], fine_detail['Lon'].iloc[inc]])
features = []
for i in range(len(fine_detail)):
    if i<len(fine_detail)-1:
        position=np.array([fine_detail['Lat'].iloc[i], fine_detail['Lon'].iloc[i]])
        next_position=np.array([fine_detail['Lat'].iloc[i+1], fine_detail['Lon'].iloc[i+1]])
        angle=bearing(position,next_position)
    feature = {
      'type': 'Feature',
      'geometry': {
        'type': 'Point',
        'coordinates': [fine_detail['Lat'].iloc[i], fine_detail['Lon'].iloc[i]]
      },
      'properties': {
          'icon': 'marker',
                  'iconstyle':{
                      'iconUrl': Path("./Generation Scripts/").joinpath(rfindex[indexinground(angle,base=1)][0]).as_posix(),
                      'iconSize': [100, 100],
                      'fillOpacity': 1},
                  
          'time': fine_detail.index[i].strftime('%Y-%m-%d %X')
      }
    }
    features.append(feature)
    features.append({
        'type': "Feature",
        'properties':{
            'name': 'Ground Track',
            'style': {'color': 'red', 'weight': 6},
            'times': [fine_detail.index[i].strftime('%Y-%m-%d %X')]*i},

        'geometry':{
            'type': "LineString",
            'coordinates': coords[i]}
        })

# Create the GeoJSON object
geojson = {
  'type': 'FeatureCollection',
  'features': features
}
from pathlib import Path
# Create the Folium map
white_url = Path('../Kingdom of the White Map/Kingdom Of the WhiteScaled.png')
white_url2 = Path('../Kingdom of the White Map/Kingdom Of the White.png')
# Create a map centered at a specific location
tile_url = Path('./Kingdom of the White Map/tiles/{z}/{x}/{-y}.png')
tile_url2 = Path('./World Map/tileshires/{z}/{x}/{-y}.png')
# Create a map centered at a specific location
m = folium.Map(location=[70, -90], zoom_start=6, min_zoom=1, max_zoom=10,control_scale = True,tiles=None)
folium.TileLayer(tiles=tile_url.as_posix(),attr='Russell',crs='EPSG3857', name='Kingdom of the White',zoom_start=6, min_zoom=1, max_zoom=10,).add_to(m)
folium.TileLayer(tiles=tile_url2.as_posix(),attr='Russell',crs='EPSG3857', name='World Map',zoom_start=6, min_zoom=1, max_zoom=10,).add_to(m)
ship_fg = folium.FeatureGroup(name='Fortuna Rubrum')
# Add the animated marker to the map
TimestampedGeoJson(
                   data=geojson,
    period='PT1H',
    duration='PT1M',
    auto_play=True,
    loop=False,
    loop_button=True,
    date_options='YYYY/MM/DD',).add_to(m)

m.add_child(ship_fg)
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
current_location=[69.86375,-89.86954]
ship_fg = folium.FeatureGroup(name='Fortuna Rubrum')
#folium.Marker(location=current_location,
#              popup='Ship Location',
#              tooltip='Fortuna Rubrum <br> Docked at Storm Castle <br> 21 Knights <br> 3 Archers <br> Zepplin Crew <br> Medical Crew',
#              icon=folium.features.CustomIcon(icon_image=redfortune_url.as_posix(), icon_size=(2*72, 2*50))).add_to(ship_fg)

folium.LayerControl().add_to(m)
# Display the map
m.save("../test.html")
