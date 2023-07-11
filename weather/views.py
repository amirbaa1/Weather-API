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
        weather = {
            'city': city_name,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        return render(request, 'home.html', context={'weather': weather})
