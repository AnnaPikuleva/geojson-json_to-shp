import argparse
import geopandas as gpd
import glob
import os

parser = argparse.ArgumentParser(description='convert')
parser.add_argument("--out_folder")
parser.add_argument("--path")

args = parser.parse_args()

folder_geojson = args.out_folder
folder_shp = args.path

files = glob.glob(folder_geojson + '*.geojson') 
for filename in files:
    file_name = os.path.basename(filename)
    a = os.path.splitext(file_name)[0]
    df = gpd.read_file(filename)
    shp_file_path = os.path.join(folder_shp,a +'.shp')
    print(shp_file_path)
    df.to_file(shp_file_path)

