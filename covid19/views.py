from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

# Create your views here.

global head , foot
head = '<!doctype html> <html lang="en"><head><!-- Required meta tags --><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><!-- Bootstrap CSS --><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous"><link rel="icon" type="image" href="https://django-covid19-tracker.herokuapp.com/static/covid.ico"><!-- font awesome cdn --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@5.15.3/css/fontawesome.min.css" integrity="sha384-wESLQ85D6gbsF459vf1CiZ2+rr+CsxRY0RpiF1tLlQpDnAgg6rwdsUF1+Ics2bni" crossorigin="anonymous"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> <style> html {scroll-behavior: smooth;body{overflow-x: hidden;}.searchField input{width: 90vw;margin: auto}.footer{color: whitesmoke;.footer a{text-decoration: none;color: whitesmoke !important;.fa{cursor: pointer;}</style></head><body><header><nav class="navbar navbar-expand-lg navbar-dark bg-dark"><div class="container-fluid"><a class="navbar-brand" href="/"><img src="https://django-covid19-tracker.herokuapp.com/static/covid.ico" alt=""  class="d-inline-block align-text-top">Covid Tracker</a><button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarNav"><ul class="navbar-nav ms-auto mb-2 mb-lg-0"><li class="nav-item"><a class="nav-link active" aria-current="page" href="/">Home</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/world">World</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/india">India</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/helplines">Helplines</a></li><li class="nav-item"><a class="nav-link active" aria-current="page" href="/bedAvailability">Bed Availability</a></li></ul></div></div></nav></header> <br> <br ><div class="container">'

foot = '</div><footer class="page-footer font-small bg-dark" style="color:white;"><div class="d-flex justify-content-center"><div class="footer mt-auto pt-3 pb-0 bg-dark" >Made with ❤ and &#60;/code&gt; by<a href="https://www.instagram.com/yaarteracoder/" style="color:white; text-decoration:none; "> Harsh Lad</a></div></div><div class="footer mt-auto pt-3 pb-2 bg-dark d-flex justify-content-center"><a target="_blank" href="https://www.instagram.com/yaarteracoder/"style="color:white; text-decoration:none;"> <i class="fa fa-instagram mx-4"></i> </a><a target="_blank" href="https://twitter.com/harshlad101"style="color:white; text-decoration:none;"> <i class="fa fa-twitter mx-4"></i> </a><a target="_blank" href="https://github.com/Harsh-Lad"style="color:white; text-decoration:none;"> <i class="fa fa-github mx-4"></i> </a><a target="_blank" href="https://www.facebook.com/profile.php?id=100009517594580"style="color:white; text-decoration:none;"> <i class="fa fa-facebook mx-4"></i> </a><a target="_blank" style="color:white; text-decoration:none;" href="mailto: yaarteracoder@gmail.com"><i class="fa fa-envelope mx-4"></i> </a></div></div></footer><script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js" integrity="sha384-SR1sx49pcuLnqZUnnPwx6FCym0wLsk5JZuNx2bPPENzswTNFaQU1RDvt3wT4gWFG" crossorigin="anonymous"></script><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.min.js" integrity="sha384-j0CNLUeiqtyaRmlzUHCPZ+Gy5fQu0dQ6eZ/xAww941Ai1SxSY+0EQqNXNE6DZiVc" crossorigin="anonymous"></script><script>$(document).ready(function()\n{$(".container").addClass(\'table-responsive\'); $("#tablegrid").addClass(\'table table-striped table-hover border\');});</script> '


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
    try:
        url = "https://bbmpgov.com/chbms/"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find(id ='D')
        table = table.prettify()
        table = head+table+foot
        return HttpResponse(table)
    except:
        table = "<h1>The Government Website is down please try again later</h1>"
        table = head+table+foot
        return HttpResponse(table)


def vadodara(request):
    try:
        url = "https://vmc.gov.in/Covid19VadodaraApp/HospitalBedsDetails.aspx?tid=13"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find(id = 'ContentPlaceHolder1_GVHospSegment1')
        table = table.prettify()
        table = head+table+foot
        return HttpResponse(table)
    except:
        table = "<h1>The Government Website is down please try again later</h1>"
        table = head+table+foot
        return HttpResponse(table)

def pune(request):
    try:
        url = "https://www.divcommpunecovid.com/ccsbeddashboard/hsr"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find(id='tablegrid')
        table = table.prettify()
        table = head+table+foot
        return HttpResponse(table)
    except:
        table = "<h1>The Government Website is down please try again later</h1>"
        table = head+table+foot
        return HttpResponse(table)

def uttarPradesh(request):
    try:
        url = "http://dgmhup.gov.in/en/CovidReport"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find(id ='MainContent_EN_grd_data')
        table = table.prettify()
        table = head+table+foot
        return HttpResponse(table)
    except:
        table = "<h1>The Government Website is down please try again later</h1>"
        table = head+table+foot
        return HttpResponse(table)

def uttarakhand(request):
    try:
        url = "https://covid19.uk.gov.in/bedssummary.aspx"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find(id = 'grdhospitalbeds')
        table = table.prettify()
        table = head+table+foot
        return HttpResponse(table)
    except:
        table = "<h1>The Government Website is down please try again later</h1>"
        table = head+table+foot
        return HttpResponse(table)


def nagpur(request):
    try:
        url = "http://nsscdcl.org/covidbeds/AvailableHospitals.jsp"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find(id ='example1')
        table = table.prettify()
        table = head+table+foot
        return HttpResponse(table)
    except:
        table = "<h1>The Government Website is down please try again later</h1>"
        table = head+table+foot
        return HttpResponse(table)

