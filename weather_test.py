from config import WEATHER_TOKEN
import requests

lat,lon=45.09017208208641, 39.04098228220222
base_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_TOKEN}&units=metric'
response=requests.get(base_url)
answer=response.json()
print(answer)

lat,lon=39.74354874351326, -105.51640168994476
base_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_TOKEN}&units=metric'
response=requests.get(base_url)
answer=response.json()
print(answer)

lat,lon= -11.725612569823952, -57.41246950733
base_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_TOKEN}&units=metric'
response=requests.get(base_url)
answer=response.json()
print(answer)

lat,lon= -10.260570873973654, 29.525775412385894
base_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_TOKEN}&units=metric'
response=requests.get(base_url)
answer=response.json()
print(answer)

lat,lon= -30.586644131699423, 133.83246915893974
base_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_TOKEN}&units=metric'
response=requests.get(base_url)
answer=response.json()
print(answer)