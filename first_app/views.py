from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse


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
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404()
        #  return HttpResponseNotFound("This page doesn't exists.")


# def articles_redirect_view(request, num):
#     if num > len(articles):
#         raise Http404()
    
#     topic = list(articles.keys())[num]
#     return HttpResponseRedirect(topic)


def articles_redirect_view(request, num):
    if num > len(articles):
        raise Http404()
    
    topic = list(articles.keys())[num]
    return HttpResponseRedirect(reverse("topic-page", args=[topic]))


def add_view(request, num1, num2):
    """
    host/first_app/<num1>/<num2>/
    """
    result = num1 + num2
    return HttpResponse(str(result))




