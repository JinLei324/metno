from django.shortcuts import render
import requests


def index(request):
    headers = {'user-agent': 'metno/0.0.1'}
    response = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=-0.25", headers=headers)
    
    context = {
        'a': 'sample'
    }
    return render(request, 'index.html', context)