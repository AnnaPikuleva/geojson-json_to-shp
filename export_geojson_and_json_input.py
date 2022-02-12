import geopandas as gpd
import glob
import os
import pandas as pd
import json

out_folder = input ('путь к папке, где лежать файлы')
path_gejson = input ('путь для сохранения папки с shp')
path_json = input ('путь для сохранения папки с shp')

a_files = glob.glob(out_folder + '/*.geojson')
for filename in a_files:
    #возвращаем имя пути
    file_name = os.path.basename(filename)
    a = os.path.splitext(file_name)[0]
    #прочиать geojson
    df = gpd.read_file(filename)
    shp_file_path = os.path.join(path_gejson,a +'.shp')
    df.to_file(shp_file_path) 

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
        dff, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    gdf.to_file(shp_file_path) 

