from django.shortcuts import render
from django.http import HttpResponse


def mysite(request):
    return HttpResponse("MySite")