from django.shortcuts import render
import requests
from .models import City_weather
from .forms import CitiesForm


def main_weather(request):
    appid = '653136b757efafd9392091c66d7c7fa3'

    if request.method == 'POST':
        form = CitiesForm(request.POST)
        form.save()

    form = CitiesForm

    cities = City_weather.objects.all()
    all_cities = []
    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appid}"
        info = requests.get(url).json()
        city_weather = {
            'city': city,
            'temperature': info['main']['temp'],
            'icon': info['weather'][0]['icon']}
        all_cities.append(city_weather)
    context = {'info': all_cities, 'form': form}

    return render(request, 'weather/weather_main.html', context)



