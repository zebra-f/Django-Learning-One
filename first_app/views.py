from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

articles = {
    "programming": "Programming page",
    "cars": "Cars page"
}


def simple_view(request):
    """
    host/first_app/
    """
    return HttpResponse("Simple View")


def sports_view(request):
    """
    host/first_app/sports/
    """
    return HttpResponse("Sports Page")


def finance_view(reqeust):
    """
    host/first_app/finance/
    """
    return HttpResponse("Finance Page")


def articles_view(request, topic):
    """
    host/first_app/<topic>/
    """
    return HttpResponse(articles[topic])





