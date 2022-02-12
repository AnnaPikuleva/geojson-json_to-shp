Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #���, ������� ������������ geojson � json � shp c ������ ������ ����� argparse

import argparse
import geopandas as gpd
import glob
import os
import pandas as pd
import json

parser = argparse.ArgumentParser(description='convert')

parser.add_argument("--out_folder")
parser.add_argument("--path_geojson")
parser.add_argument("--path_json")

args = parser.parse_args()

folder = args.out_folder
folder_shp_geojson = args.path_geojson
folder_shp_json = args.path_json


a_files = glob.glob(folder + '/*.geojson')
for filename in a_files:
    #���������� ��� ����
    file_name = os.path.basename(filename)
    a = os.path.splitext(file_name)[0]
    #�������� geojson
    df = gpd.read_file(filename)
    shp_file_path = os.path.join(folder_shp_geojson,a +'.shp')
    df.to_file(shp_file_path) 

b_files = glob.glob(folder + '/*.json')
for filename in b_files:
    #���������� ��� �����
    file_name = os.path.basename(filename)
    #���������� ��� �����
    a = os.path.splitext(file_name)[0]
    #�������� json
    dff = pd.read_json(filename)  
    #���� ���� ��������� json
    shp_file_path = os.path.join(folder_shp_json,a +'.shp')
    gdf = gpd.GeoDataFrame(
        dff, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    gdf.to_file(shp_file_path) 
