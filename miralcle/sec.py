# Forecast
import http.client

conn = http.client.HTTPSConnection("weather-api167.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "acd682c32emshf18680e33b63910p11ee92jsn095b92ea768a",
    'x-rapidapi-host': "weather-api167.p.rapidapi.com",
    'Accept': "application/json"
}

conn.request("GET", "/api/weather/forecast?place=London%2CGB&cnt=3&units=standard&type=three_hour&mode=json&lang=en", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# Normal wether
import http.client

conn = http.client.HTTPSConnection("weather-api167.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "acd682c32emshf18680e33b63910p11ee92jsn095b92ea768a",
    'x-rapidapi-host': "weather-api167.p.rapidapi.com",
    'Accept': "application/json"
}

conn.request("GET", "/api/weather/current?place=London%2CGB&units=standard&lang=en&mode=json", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))