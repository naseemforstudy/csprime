from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns=[
    path('index/',views.index,name='index'),
    path('checkPrime/',views.checkPrime,name='check_prime')
]