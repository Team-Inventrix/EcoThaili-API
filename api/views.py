from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def eco_api(request):
    return HttpResponse("Hello, EcoApi!!")
