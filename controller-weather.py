# Controls flow #
from weather import WeatherObject

weather = WeatherObject()

value = input("Specify weather detail you want to know:\n")

answer = weather.get_weather_detail(value)

print(f'{value}: {answer}')
