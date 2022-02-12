import geopandas as gpd
import glob
import os
import pandas as pd
import json

out_folder = input ('���� � �����, ��� ������ �����')
path_gejson = input ('���� ��� ���������� ����� � shp')
path_json = input ('���� ��� ���������� ����� � shp')

a_files = glob.glob(out_folder + '/*.geojson')
for filename in a_files:
    #���������� ��� ����
    file_name = os.path.basename(filename)
    a = os.path.splitext(file_name)[0]
    #�������� geojson
    df = gpd.read_file(filename)
    shp_file_path = os.path.join(path_gejson,a +'.shp')
    df.to_file(shp_file_path) 

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
        dff, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    gdf.to_file(shp_file_path) 

