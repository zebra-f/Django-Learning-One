from django.urls import path

from . import views


urlpatterns = [
    path('', views.simple_view),
    path('sports/', views.sports_view),
    path('finance/', views.finance_view),
    path('<topic>/', views.articles_view),
    
]       