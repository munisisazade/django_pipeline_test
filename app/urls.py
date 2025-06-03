# from django.contrib import admin
from django.urls import path
from app.views import home_page

urlpatterns = [
    path("", home_page, name="home"),
]
