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

def karnataka(request):
    url = "https://bbmpgov.com/chbms/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find(id ='D')
    table = table.prettify()
    new = "new variableeeeeeeeeeeeeeee"
    return HttpResponse(table)


def vadodara(request):
    url = "https://vmc.gov.in/Covid19VadodaraApp/HospitalBedsDetails.aspx?tid=13"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find_all(class_ = 'col-lg-12')[1]
    """ table = table.prettify() """
    return HttpResponse(table)

def pune(request):
    url = "https://www.divcommpunecovid.com/ccsbeddashboard/hsr"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find(id='tablegrid')
    table = table.prettify()
    return HttpResponse(table)

def uttarPradesh(request):
    url = "http://dgmhup.gov.in/en/CovidReport"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find(id ='MainContent_EN_grd_data')
    table = table.prettify()
    return HttpResponse(table)
    return HttpResponse('uttarPradesh')

def uttarakhand(request):
    url = "https://covid19.uk.gov.in/bedssummary.aspx"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find(id = 'grdhospitalbeds')
    table = table.prettify()
    return HttpResponse(table)

def nagpur(request):
    url = "http://nsscdcl.org/covidbeds/AvailableHospitals.jsp"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find(id ='example1')
    table = table.prettify()
    print(table)
    return HttpResponse(table)
