from django.contrib import admin
from django.urls import path
from . import views
#All linkchops app url is registered here. 
urlpatterns = [
    path('', views.index, name="index"), 
]