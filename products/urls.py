"""
This is called URL mapping
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]
