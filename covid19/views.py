from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):
    data = True
    result = None
    globalData = None
    countries = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            globalData = result.json()['Global']
            countries = result.json()['Countries']
            data = False
        except:
            data = True
    param = {'globalData':globalData, 'countries':countries}
    return render(request,'index.html',param)