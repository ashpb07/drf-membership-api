from django.contrib import admin
from django.urls import path
from main.views import LoginAPI,RegisterAPI,PersonAPI

urlpatterns = [
       path('login/',LoginAPI.as_view()),
    path('persons/',PersonAPI.as_view()),
    path('register/',RegisterAPI.as_view()),
]
