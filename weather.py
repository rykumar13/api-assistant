import requests
import json


class WeatherObject:
    # primary details #
    short_desc = ''
    full_desc = ''
    temp = ''
    feels_like = ''
    wind_speed = ''

    # secondary details #
    sunrise = ''
    sunset = ''
    timezone = ''
    pressure = ''
    humidity = ''
    visibility = ''
    temp_max = ''
    temp_min = ''
    longitude = ''
    latitude = ''

    def __init__(self):
        # call open-weather-map api to get data #
        url = "https://community-open-weather-map.p.rapidapi.com/weather"
        querystring = {"q": "London,uk", "lat": "0", "lon": "0", "callback": "", "id": "2172797", "lang": "null",
                       "units": "\"metric\" or \"imperial\"", "mode": "xml, html"}
        headers = {
            'x-rapidapi-key': "0fddf05837mshbfc86e466e6b7bfp147bf3jsnd3a08cbdbcc7",
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        weather_dict = json.loads(response.content)

        self.short_desc = weather_dict['weather'][0]['main']

        self.full_desc = weather_dict['weather'][0]['description']

        self.temp = weather_dict['main']['temp']

        self.feels_like = weather_dict['main']['feels_like']

        self.wind_speed = weather_dict['wind']['speed']

        self.sunrise = weather_dict['sys']['sunrise']

        self.sunset = weather_dict['sys']['sunset']

        self.timezone = weather_dict['timezone']

        self.pressure = weather_dict['main']['pressure']

        self.humidity = weather_dict['main']['humidity']

        self.visibility = weather_dict['visibility']

        self.temp_max = weather_dict['main']['temp_max']

        self.temp_min = weather_dict['main']['temp_min']

        self.longitude = weather_dict['coord']['lon']

        self.latitude = weather_dict['coord']['lat']

    def get_weather_detail(self, value):
        switcher = {
            'short_desc': self.short_desc,
            'full_desc': self.full_desc,
            'temp': self.temp,
            'feels_like': self.feels_like,
            'wind_speed': self.wind_speed,
            'sunrise': self.sunrise,
            'sunset': self.sunset,
            'timezone': self.timezone,
            'pressure': self.pressure,
            'humidity': self.humidity,
            'visibility': self.visibility,
            'temp_max': self.temp_max,
            'temp_min': self.temp_min,
            'longitude': self.longitude,
            'latitude': self.latitude,
        }
        return switcher.get(value, 'invalid weather detail')
