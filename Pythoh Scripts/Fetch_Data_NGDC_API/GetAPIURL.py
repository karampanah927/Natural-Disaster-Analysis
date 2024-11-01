import requests
import json
content = requests.get("https://www.ngdc.noaa.gov/hazel/hazard-service/docs/api.json")
myjson = content.json()
for api in myjson['paths'].keys():
	tag = myjson['paths'][api]['get']['tags'][0]


# for idx,pair in enumerate(apis.items()):
# 	print(idx,pair[0],pair[1])
for i in myjson['paths'].keys():
	print(f"self.{myjson['paths'][i]['get']['summary'].replace(' ','_').lower()} = '{i}'")

