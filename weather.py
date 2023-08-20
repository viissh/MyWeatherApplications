import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int

load_dotenv()
api_key = os.getenv('API_KEY')
#print(api_key)

def get_lat_long(city_name,state_code,country_code,API_key):
    a='//'
    b='/'
    #resp = requests.get("https:"+a+"api.openweathermap.org"+b+"geo"+b+"1.0"+b+"direct?q={city_name},{state_code},{country_code}&appid={API_key}")
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat,lon

def getCurrentWeather(lat,lon,API_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data = WeatherData(
        main = response.get('weather')[0].get('main'),
        description = response.get('weather')[0].get('description'),
        icon = response.get('weather')[0].get('icon'),
        temperature = int(response.get('main').get('temp'))
    )

    return data

def main(city_name,state_code,country_code):
    lat,lon = get_lat_long(city_name,state_code,country_code,api_key)
    weather_data = getCurrentWeather(lat,lon,api_key)
    return weather_data

if __name__ == '__main__':
    lat,lon = get_lat_long('Dhanbad','Jharkhand','India',api_key)
    print(getCurrentWeather(lat,lon,api_key))