from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    data = True
    result = None
    globalData = None
    while(data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            globalData = result.json()['Global']
            data = False
        except:
            data = True
    param = {'globalData':globalData}
    return render(request,'index.html',param)

def world(request):
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
    return render(request,'world.html',param)

def india(request):
    indiaResults = requests.get('https://api.covid19india.org/data.json')
    stateResult = indiaResults.json()['statewise']
    param = {'state':stateResult}
    return render(request,'country.html',param)

def helplines(request):
    helpline = requests.get('https://api.rootnet.in/covid19-in/contacts')
    helplineData = helpline.json()['data']['contacts']['regional']
    param = {'helpline':helplineData}
    return render(request,'helplines.html',param)


def bedAvailability(request):
    return render(request,'bedAvailability.html')

def chhattisgarh(request):
    url = "https://cg.nic.in/health/covid19/RTPBedAvailable.aspx"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.prettify())
    return HttpResponse('chhattisgarh')

def naviMumbai(request):
    url = requests.get("https://nmmchealthfacilities.com/HospitalInfo/showhospitalist")
    soup = BeautifulSoup(url.content, 'html.parser')
    divSocial = soup.find_all("h4")
    divVacant = soup.find_all("div",class_ ="bg-gradient-success")
    vacList = []
    availBed = []
    i,j = 1,0
    while i < 44 and j < 43:
        mainTxt = divSocial[i].find('b')
        vacTxt = divVacant[j].find('b')
        vacItem = mainTxt.find(text=True)
        vacBed = vacTxt.find(text=True)
        vacList.append(vacItem)
        availBed.append(vacBed)
        i += 1 
        j += 1
    param = {'hospital':vacList,'bed':availBed}
    return render(request,'naviMumbai.html', param)

def pune(request):
    return HttpResponse('pune')

def uttarPradesh(request):
    return HttpResponse('uttarPradesh')

def uttarakhand(request):
    return HttpResponse('uttarakhand')

def delhi(request):
    return HttpResponse('delhi')