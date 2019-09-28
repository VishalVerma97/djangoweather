# This is my views.py file
from django.shortcuts import render

# Create your views here.


def home(request):
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2019-09-28&distance=25&API_KEY=B90E89A0-0AB7-4154-BBD6-1C8616A917C6")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error ....."

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
