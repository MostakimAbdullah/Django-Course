from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse("This is the couses page.")

def about(request):
    return HttpResponse("This is the mostakim's page.")

def home(request):
    return HttpResponse("This is the first-app page.")
