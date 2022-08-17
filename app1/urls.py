from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
  
    path("",views.index,name="home"),
    path("index",views.index,name="home"),
    path("about",views.about,name="home"),
    path("contact",views.contact,name="home")
]
