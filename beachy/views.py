from django.shortcuts import render
from django.contrib import admin

# Create your views here.
def index(request):
    return render (request, 'beachy/index.html')