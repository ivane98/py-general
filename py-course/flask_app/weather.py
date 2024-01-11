from dotenv import load_dotenv
import requests
import os
from pprint import pprint

load_dotenv()



def get_current_weather(city='Tbilisi'):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print("\nGet current weather conditions")

    city = input('\nPlease enter a city name')

    weather_data = get_current_weather(city)

    print('\n')
    pprint(weather_data)
    
