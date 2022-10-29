import requests
import sqlite3

class Volcano:
	def __init__(self):
		self.url = "https://www.ngdc.noaa.gov/hazel/hazard-service"
		self.list_volcanoes = '/api/v1/volcanoes'
		self.show_volcano = '/api/v1/volcanoes/{id}'
		self.list_earthquakes = '/api/v1/volcanoes/{id}/earthquakes'
		self.volcano_details = '/api/v1/volcanoes/{id}/info'
		self.show_volcano_location_details = '/api/v1/volcanoes/{id}/location'
		self.list_references = '/api/v1/volcanoes/{id}/references'
		self.list_tsunamis_ = '/api/v1/volcanoes/{id}/tsunamis'
		# self.list_volcano_locations = '/api/v1/volcanolocs'
		self.show_volcano_location = '/api/v1/volcanolocs/{id}'
		self.complete_list_earthquakes = '/api/v1/earthquakes'
		self.show_earthquake = '/api/v1/earthquakes/{id}'



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

	def get_all_related_earthquake(self):
		fields = {"volcano_id":"string",
		          "area": "string",
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
		with open ("volcanos_EarthquakeRelated.csv",'w') as f:
			data = self.get_data(self.list_volcanoes)
			id_list = []
			for i in range(len(data)):
				id_list.append(list(data[i].values())[0])


			fields_names = '\t'.join(list(fields.keys()))
			f.write(fields_names + "\n")

			for self_id in id_list:
				data = self.get_data(self.list_earthquakes, self_id)
				for d in data:
					sample = dict.fromkeys(fields.keys(),'')# we want to copy one dictionary to
					for att,v in d.items():
						sample[att] = v
						# if att == "volcano_id":
						# 	sample[att] = self_id
						# else:
						# 	sample[att] = v
					row = '\t'.join([f"{v}" for v in sample.values()])
					f.write(row+"\n")





v = Volcano()
v.get_all_related_earthquake()



print("done")
# data = v.get_all_volcano()
# data1 = v.get_data(v.show_volcano,id = 2585)

# Volcanos_list = []
# for i in Volcanos_list:
# 	data = v.get_data(v.list_earthquakes,id = 5605)

# for i in range(1,100):
# 	data = v.get_data(v.list_earthquakesi,id = 5605)
# 	print (len(data),data)
# data = v.get_data(v.show_earthquake,id = 1787)
# print(data1)

# for i in data[1]:
# 	print(i,":",type(data[1][i]))
# print(data1)



