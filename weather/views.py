from django.shortcuts import render
from django.views import View
import requests
from .forms import FormCity
from django.db.models import Q
from .models import City


def HomeWeather(request):
    if request.method == 'GET':
        # search_c = request.GET.get('search_city')
        search_c = FormCity(request.GET)
        if search_c.is_valid():
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
            city_name = search_c.cleaned_data['name']
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
        else:
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
            city_name = 'tehran'
            api_key = '690086498ed6ebaabb81343f0cf12fb0'
            city_weather = requests.get(url.format(city_name, api_key)).json()
            weather_c = round(city_weather['main']['temp'] - 273, 2)
            weather = {
                'city': city_name,
                'country': city_weather['sys']['country'],
                'temperature': weather_c,
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            search_c = FormCity()
        return render(request, 'home.html', context={'weather':weather,'search_c': search_c})

    # if request.method == 'POST':
