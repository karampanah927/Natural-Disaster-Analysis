
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
		self.agent_list = '/api/v1/descriptors/volcano/agents'

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

	def get_all_agents(self):
		fileds = { "id": "A",
      "description": "Avalanche (Debris and landslides)"}
		with open("agents.csv","w")as f:
			data = self.get_data(self.agent_list)
			field_names = '\t'.join(list(fileds.keys()))
			f.write(field_names+"\n")

			for d in data:
				sample = dict.fromkeys(fileds.keys(),'')
				for att,v in d.items():
					sample[att]=v
				row = '\t'.join([f"{v}" for v in sample.values()])
				f.write(row+"\n")


v = Volcano()
data = v.get_all_agents()