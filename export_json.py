import geopandas as gpd
import glob
import os
import pandas as pd
import json

out_folder = input ('путь к папке, где лежать json')
path_gejson = input ('путь для сохранения папки с geojson')

b_files = glob.glob(out_folder + '/*.json')
for filename in b_files:
    #возвращаем имя файла
    file_name = os.path.basename(filename)
    #возвращаем имя файла
    a = os.path.splitext(file_name)[0]
    
    #прочиать json
    dff = pd.read_json(filename)  
    #путь куда сохранять json
    shp_file_path = os.path.join(path_json,a +'.shp')
    
    gdf = gpd.GeoDataFrame(
        dff, geometry=gpd.points_from_xy(dff.Longitude, dff.Latitude))
    gdf.to_file(shp_file_path) 
