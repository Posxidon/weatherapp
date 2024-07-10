import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
from django.conf import settings  

def index(request):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 

    form = CityForm()
    cities = City.objects.all()

    weather_data = []
    for city in cities:
        url = base_url.format(city.name, settings.OPENWEATHERMAP_API_KEY)
        r = requests.get(url).json()
        
        if 'main' not in r:
            continue
        
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'id': city.id
        }
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)

def delete_city(request, city_id):
    city = City.objects.get(id=city_id)
    city.delete()
    return redirect('index')
