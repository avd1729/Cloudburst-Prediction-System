import requests
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

API_KEY = ""

CITY = "New Delhi"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(response)
