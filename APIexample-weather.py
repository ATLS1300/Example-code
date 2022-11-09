import reqests
import json

response = requests.get('https://api.weather.gov/gridpoints/BOU/53,74/forecast ')

data = response.json()#pass the data into a json reader
#data is now a dictionary

#for weather.gov data, information is stored under the 'properties' key
#this is a nested dictionary, so data['properties'] also has keys

#we can access nested keys the same way we access nested lists:
data['properties']['periods'] #returns a list of data by segments (~12 hrs)

data['properties']['periods'][0]['shortForecast'] #returns individual forecast descriptions (str)
#data['properties']['periods'][0]['name'] #returns the time period (str)
#data['properties']['periods'][0]['temperature'] #returns the temperature of the time period (int)

