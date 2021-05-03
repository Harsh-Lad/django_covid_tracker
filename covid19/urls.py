from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path("india/", views.india, name="india"),
    path("world/", views.world, name="world"),
    path("helplines/", views.helplines, name="helplines"),
    path("bedAvailability/", views.bedAvailability, name="bedAvailability"),
    path("karnataka/", views.karnataka, name="karnataka"),
    path("vadodara/", views.vadodara , name="vadodara"),
    path("pune/", views.pune, name="pune"),
    path("uttarPradesh/", views.uttarPradesh, name="uttarPradesh"),
    path("uttarakhand/", views.uttarakhand, name="uttarakhand"),
    path("nagpur/", views.nagpur, name="nagpur"),
    
] 
