# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:37:36 2023

@author: lycea
"""

from osgeo import gdal,osr
import rasterio
ds = gdal.Open('../Kingdom of the White Map/Kingdom Of the White.png')
dst = gdal.Translate('../Kingdom of the White Map/Kingdom Of the White.tif',ds,outputSRS="EPSG:4326",outputBounds=[-93.1,73.5,-83.2,67.8])
dst=None

#raster=rasterio.open('../Kingdom of the White Map/Kingdom Of the White.tif')
#import gdal2tiles
#gdal2tiles.generate_tiles('../Kingdom of the White Map/Kingdom Of the White.tif', '../Kingdom of the White Map/tiles/', nb_processes=2, zoom='6-9')