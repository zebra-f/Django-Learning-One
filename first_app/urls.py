from django.urls import path

from . import views


urlpatterns = [
    path('', views.simple_view),
    path('sports/', views.sports_view),
    path('finance/', views.finance_view),
    path('<int:num>', views.articles_redirect_view),
    path('<str:topic>/', views.articles_view, name="topic-page"),
    path('<int:num1>/<int:num2>/', views.add_view)
]       