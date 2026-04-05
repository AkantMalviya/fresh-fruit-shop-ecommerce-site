from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# /products --> index
# Uniform Resource Locator(Address)
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {"products": products})


# Create your views here.
# views.py


def new(request):
    return HttpResponse("New Products")
