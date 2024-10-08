import requests


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "..."

weather_params = {
    "lat": 56.162937,
    "lon": 10.203921,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Husk paraplyen, det vil regne")
