from django.contrib import admin
from django.urls import path
from . import views
#All linkchops app url is registered here. 
urlpatterns = [
    path('', views.home, name="home"), 
    path('<str:shorten_code>', views.redirect_to_original, name="redirect_to_original"),
]