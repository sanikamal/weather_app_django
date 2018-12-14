import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
        # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=YOUR_API_KEY'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=631d05ff6393f7a5c5e6a68d4943d852'
    # city='Delhi'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    
    cities = City.objects.all()
    # r=requests.get(url.format(city))
    # print(r.text)
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
                'city' : city.name,
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon' : r['weather'][0]['icon'],
            }
        weather_data.append(city_weather)
    # print(city_weather)
    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html',context)
