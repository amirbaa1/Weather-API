from django.shortcuts import render
from django.views import View
import requests


def HomeWeather(request):
    if request.method == 'GET':
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        city_name = 'Tehran'
        api_key = '690086498ed6ebaabb81343f0cf12fb0'
        city_weather = requests.get(url.format(city_name, api_key)).json()
        print('---->', city_weather)
        weather_c = round(city_weather['main']['temp'] - 273, 2)
        weather = {
            'city': city_name,
            'country': city_weather['sys']['country'],
            'temperature': weather_c,
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        return render(request, 'home.html', context={'weather': weather})
    # if request.method == 'POST':

