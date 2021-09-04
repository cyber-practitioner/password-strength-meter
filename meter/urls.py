from django.urls import path,include
from django.shortcuts import redirect
from . import views
from django.contrib.auth import authenticate, login,logout

urlpatterns = [
    path('home', views.home,name='home-page'),
    path('result', views.result,name='result-page'),
]