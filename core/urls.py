from django.urls import path
from . import views


core_urls = [
    path('', views.index, name='index'),
]