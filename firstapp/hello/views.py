from django.shortcuts import render
from django.https import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")