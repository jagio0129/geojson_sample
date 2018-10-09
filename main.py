# coding: UTF-8

import json
import os
from shapely.geometry import shape, Point

SOURCE_PATH = os.path.dirname(os.path.abspath(__file__))
GEO_JSON    = SOURCE_PATH + "/tokyo.geojson"

# 任意の位置情報がどの市区町村に属するか判定するメソッド
def belong(geo_json, lat, lon):
  point = Point(lon, lat)
  for feature in geo_json['features']:
    polygon = shape(feature['geometry'])
    if polygon.contains(point):
        return feature['properties']['N03_004']
  return None

### main
if __name__ == '__main__':

  f = open(GEO_JSON,'r')
  geo_json = json.load(f)

  # 東京駅
  lat = 35.681167
  lon = 139.767052
  city = belong(geo_json, lat, lon)
  print(city)

  # 東京スカイツリー
  lat = 35.710063
  lon = 139.8107
  city = belong(geo_json, lat, lon)
  print(city)

  # 小笠原村
  lat = 27.094366
  lon = 142.191918
  city = belong(geo_json, lat, lon)
  print(city)

  # 大阪 梅田
  lat = 34.699134
  lon = 135.495218
  city = belong(geo_json, lat, lon)
  print(city)
