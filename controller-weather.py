# Controls flow #
from weather import WeatherObject

weather = WeatherObject()

value = input("Specify weather detail you want to know:\n")

while not(value == 'exit'):
    answer = weather.get_weather_detail(value)
    print(f'{value}: {answer}')
    value = input("Specify weather detail you want to know:\n")
