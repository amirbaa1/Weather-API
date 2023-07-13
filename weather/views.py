from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.views import View
import requests
from .forms import FormCity
from .models import City
import datetime
import json


def HomeWeather(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    url_5h = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric'
    city_name = 'Tehran'
    api_key = '690086498ed6ebaabb81343f0cf12fb0'

    city_weather = requests.get(url.format(city_name, api_key)).json()
    city_weather_5day = requests.get(url_5h.format(city_name, api_key)).json()
    # print('--->',city_weather_5day)
    weather_5 = []
    temperature_dict = {}
    #############
    for i in city_weather_5day['list']:
        timestamp = i['dt_txt']
        dt = datetime.datetime.fromisoformat(timestamp)
        formatted_dt = dt.strftime("%A %H")
        temperature = int(i['main']['temp'])
        print(f"زمان: {formatted_dt} - دما: {temperature}°C")

        day = formatted_dt.split(' ')[0]
        hour = formatted_dt.split(' ')[1]

        if day not in temperature_dict:
            temperature_dict[day] = []

        temperature_dict[day].append(temperature)

    for day, temperatures in temperature_dict.items():
        mean_temp = int(sum(temperatures) / len(temperatures))
        # print(f"روز: {day}")
        # print(f"میانگین دما: {mean_temp}°C")
        # print('-----')
        weather_5.append({'day': day, 'mean_temp': mean_temp, 'icon': city_weather['weather'][0]['icon']})

    ##################

    weather = {
        'city': city_name,
        'country': city_weather['sys']['country'],
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']  # not is real icon !!!
    }

    search_c = FormCity()

    return render(request, 'home.html', context={'weather': weather, 'search_c': search_c, 'weather_5': weather_5})


def search_city(request):
    if request.method == "POST":
        searched = request.POST['searched']
        try:
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
            url_5h = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric'
            # city_name = searched.cleaned_data['name']

            api_key = '690086498ed6ebaabb81343f0cf12fb0'
            city_weather = requests.get(url.format(searched, api_key)).json()
            city_weather_5day = requests.get(url_5h.format(searched, api_key)).json()

            print('---->', city_weather)
            #######
            weather = {
                'city': searched,
                'country': city_weather['sys']['country'],
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_5 = []
            temperature_dict = {}

            for i in city_weather_5day['list']:
                timestamp = i['dt_txt']
                dt = datetime.datetime.fromisoformat(timestamp)
                formatted_dt = dt.strftime("%A %H")
                temperature = int(i['main']['temp'])
                print(f"زمان: {formatted_dt} - دما: {temperature}°C")

                day = formatted_dt.split(' ')[0]
                hour = formatted_dt.split(' ')[1]

                if day not in temperature_dict:
                    temperature_dict[day] = []

                temperature_dict[day].append(temperature)

            for day, temperatures in temperature_dict.items():
                mean_temp = int(sum(temperatures) / len(temperatures))
                # print(f"روز: {day}")
                # print(f"میانگین دما: {mean_temp}°C")
                # print('-----')
                weather_5.append({
                    'day': day,
                    'mean_temp': mean_temp,
                    # 'weather_icon': city_weather['weather'][0]['icon']  # not is real icon !!!

                })
                print(",,,", weather_5)
        except KeyError:
            return HttpResponseNotFound(render(request, 'search.html', {'message': "City not found."}))
    else:
        return HttpResponseNotFound(render(request, 'search.html', {'message': "City not found."}))
    return render(request, 'home.html', context={'weather': weather, 'weather_5': weather_5})
