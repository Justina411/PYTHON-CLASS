import http.client
import json

# Connect to the API host
conn = http.client.HTTPSConnection("weather-api167.p.rapidapi.com")

# Define request headers
headers = {
    'x-rapidapi-key': "25a7036a9bmsh047e233f35fba9ap1752a2jsnb89ff73c8e94",
    'x-rapidapi-host': "weather-api167.p.rapidapi.com",
    'Accept': "application/json"
}

# Make the GET request
conn.request("GET", "/api/weather/current?place=enugu,NG&units=standard&lang=en&mode=json", headers=headers)

# Read and decode the response
res = conn.getresponse()
data = res.read()
weather = json.loads(data.decode("utf-8"))

# Safely extract and print weather details
print("===== Weather Information =====")
print("Location:", weather.get("name"), "-", weather.get("sys", {}).get("country"))
print("Coordinates: Lat =", weather.get("coord", {}).get("lat"), ", Lon =", weather.get("coord", {}).get("lon"))

weather_main = weather.get("weather", [{}])[0].get("main")
description = weather.get("weather", [{}])[0].get("description")
print("Condition:", weather_main, "-", description)

print("Temperature:", weather.get("main", {}).get("temp"), "K")
print("Feels Like:", weather.get("main", {}).get("feels_like"), "K")
print("Humidity:", weather.get("main", {}).get("humidity"), "%")
print("Pressure:", weather.get("main", {}).get("pressure"), "hPa")

print("Wind Speed:", weather.get("wind", {}).get("speed"), "m/s")
print("===============================")