import geopandas as gpd
import glob
import os
import pandas as pd
import json

out_folder = input ('���� � �����, ��� ������ json')
path_gejson = input ('���� ��� ���������� ����� � geojson')

b_files = glob.glob(out_folder + '/*.json')
for filename in b_files:
    #���������� ��� �����
    file_name = os.path.basename(filename)
    #���������� ��� �����
    a = os.path.splitext(file_name)[0]
    
    #�������� json
    dff = pd.read_json(filename)  
    #���� ���� ��������� json
    shp_file_path = os.path.join(path_json,a +'.shp')
    
    gdf = gpd.GeoDataFrame(
        dff, geometry=gpd.points_from_xy(dff.Longitude, dff.Latitude))
    gdf.to_file(shp_file_path) 
