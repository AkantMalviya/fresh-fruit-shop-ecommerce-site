from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import os
from django.conf import settings
import json




# /products --> index
# Uniform Resource Locator(Address)
def index(request):
    products = [
  {
    "name": "Banana",
    "price": 40.0,
    "stock": 200,
    "image": "images/banana.png"
  },
  {
    "name": "Apple",
    "price": 60.0,
    "stock": 150,
    "image": "images/apple.png"
  },
  {
    "name": "Mango",
    "price": 120.0,
    "stock": 60,
    "image": "images/mango.png"
  },
  {
    "name": "Grapes",
    "price": 30.0,
    "stock": 500,
    "image": "images/grapes.png"
  },
  {
    "name": "Strawberry",
    "price": 150.0,
    "stock": 200,
    "image": "images/berry.png"
  },
  {
    "name": "Orange",
    "price": 50.0,
    "stock": 300,
    "image": "images/orange.png"
  },
  {
    "name": "Watermelon",
    "price": 90.0,
    "stock": 40,
    "image": "images/melon.png"
  },
  {
    "name": "Papaya",
    "price": 70.0,
    "stock": 45,
    "image": "images/papaya.png"
  },
  {
    "name": "Pomegranate",
    "price": 210.0,
    "stock": 320,
    "image": "images/pomegranate.png"
  }
]

    #products = Product.objects.all()
    return render(request, 'index.html', {"products": products})


# Create your views here.
# views.py


def new(request):
    return HttpResponse("New Products")
