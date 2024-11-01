import requests
import sqlite3

class Earthquake:
	def __init__(self):
		self.url = "https://www.ngdc.noaa.gov/hazel/hazard-service"
		self.list_earthquakes = "/api/v1/earthquakes"
		self.list_reference = "/api/v1/earthquakes/{id}/references"
		self.earthquake_tsunami_related = "/api/v1/earthquakes/{id}/tsunamis"
		self.earthquake_volcano_related = "/api/v1/earthquakes/{id}/volcanoes"

	def get_data(self,apiUrl,id = None):
		if id:
			apiUrl = self.url+apiUrl.format(id = id)
		else:
			apiUrl = self.url+apiUrl
		response = requests.request("GET", apiUrl)
		response = response.json()
		if 'items' in response:
			return response['items']
		else:
			return response

	# def creat_table(self):
	# 	conn = sqlite3.connect("NaturalDisaster.sql")
	# 	c = conn.cursor()
	#
	#
	# 	create_table_sql = """ CREATE TABLE IF NOT EXISTS Volcano (
	# 	                                        id integer PRIMARY KEY,
	# 						year integer,
	# 						month integer,
	# 						day integer,
	# 						earthquakeEventId integer,
	# 						volcanoLocationId integer,
	# 						name text,
	# 						location text,
	# 						country text,
	# 						latitude float,
	# 						longitude float,
	# 						elevation integer,
	# 						morphology text,
	# 						deathsAmountOrder integer,
	# 						damageAmountOrder integer,
	# 						housesDestroyedAmountOrder integer,
	# 						deathsAmountOrderTotal integer,
	# 						damageAmountOrderTotal integer,
	# 						housesDestroyedAmountOrderTotal integer,
	# 						significant : <class 'bool'>
	# 						publish : <class 'bool'>
	# 						status text,
	# 						timeErupt text,
	# 	                                    ); """
	#
	# 	c.execute(create_table_sql)

	def get_all_earthquakes(self):
		fileds = {"area": "string",
		      "country": "string",
		      "damageAmountOrder": 0,
		      "damageAmountOrderTotal": 0,
		      "damageMillionsDollars": 0,
		      "damageMillionsDollarsTotal": 0,
		      "day": 0,
		      "deaths": 0,
		      "deathsAmountOrder": 0,
		      "deathsAmountOrderTotal": 0,
		      "deathsTotal": 0,
		      "eqDepth": 0,
		      "eqMagMb": 0,
		      "eqMagMfa": 0,
		      "eqMagMl": 0,
		      "eqMagMs": 0,
		      "eqMagMw": 0,
		      "eqMagUnk": 0,
		      "eqMagnitude": 0,
		      "hour": 0,
		      "housesDamaged": 0,
		      "housesDamagedAmountOrder": 0,
		      "housesDamagedAmountOrderTotal": 0,
		      "housesDamagedTotal": 0,
		      "housesDestroyed": 0,
		      "housesDestroyedAmountOrder": 0,
		      "housesDestroyedAmountOrderTotal": 0,
		      "housesDestroyedTotal": 0,
		      "id": 0,
		      "injuries": 0,
		      "injuriesAmountOrder": 0,
		      "injuriesAmountOrderTotal": 0,
		      "injuriesTotal": 0,
		      "intensity": 0,
		      "latitude": 0,
		      "locationName": "string",
		      "longitude": 0,
		      "minute": 0,
		      "missing": 0,
		      "missingAmountOrder": 0,
		      "missingAmountOrderTotal": 0,
		      "missingTotal": 0,
		      "month": 0,
		      "publish": "true",
		      "regionCode": 0,
		      "second": 0,
		      "tsunamiEventId": 0,
		      "volcanoEventId": 0,
		      "year": 0}
		with open("earthquakes.csv","w")as f:
			data = self.get_data(self.list_earthquakes)
			field_names = '\t'.join(list(fileds.keys()))
			f.write(field_names+"\n")

			for d in data:
				sample = dict.fromkeys(fileds.keys(),'')
				for att,v in d.items():
					sample[att]=v
				row = '\t'.join([f"{v}" for v in sample.values()])
				f.write(row+"\n")


e = Earthquake()
data = e.get_all_earthquakes()