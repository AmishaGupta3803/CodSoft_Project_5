import requests
import key

api_key = key.apikey
city = input("Enter the city or code to view weather: ")
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
result = response.json()
temp = result["main"]["temp"]
humidity = result["main"]["humidity"]
description = result["weather"][0]["description"]
wind_speed = result["wind"]["speed"]
print(f"The temperature of {city} is {temp} Kelvin with humidity {humidity} and wind speed {wind_speed}. Also there will be {description}.")
