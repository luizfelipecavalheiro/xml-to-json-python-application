import json
import xmltodict


with open("GioMovies.xtm") as xml_file:
	
    data_dict = xmltodict.parse(xml_file.read())
	

json_data = json.dumps(data_dict, indent = 4)
	

with open("GioMovies.json", "w") as json_file:
    json_file.write(json_data)

