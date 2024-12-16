import os

import requests

key = os.getenv("WEATHER_API_KEY")
print(key)
geo_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q=Kyiv,UKR&limit=1&appid={key}")
print(geo_response.json())
# print(lat, lon)
# url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"