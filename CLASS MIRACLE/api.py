# import http.client
# import json

# conn = http.client.HTTPSConnection("weather-api167.p.rapidapi.com")

# headers = {
#     'x-rapidapi-key': "d9a042330cmshfb123a61278bd32p1175ddjsnf219f125e45b",
#     'x-rapidapi-host': "weather-api167.p.rapidapi.com",
#     'Accept': "application/json"
# }

# conn.request("GET", "/api/weather/current?place=London%2CGB&units=standard&lang=en&mode=json", headers=headers)

# res = conn.getresponse()
# data = res.read()


# weather = json.load(data.decode("utf-8"))

# print("=== weather Info ====")
# print("summ:", weather.get("coord",{}).get("lat"))


import requests

url = "https://weather-api167.p.rapidapi.com/api/weather/current"

querystring = {"place":"London,GB","units":"standard","lang":"en","mode":"json"}

headers = {
	"x-rapidapi-key": "d9a042330cmshfb123a61278bd32p1175ddjsnf219f125e45b",
	"x-rapidapi-host": "weather-api167.p.rapidapi.com",
	"Accept": "application/json"
}

response = requests.get(url, headers=headers, params=querystring)


print(response.json())iekk