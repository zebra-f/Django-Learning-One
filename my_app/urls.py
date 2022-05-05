from django.urls import path

from . import views


app_name = "my_app"

urlpatterns = [
    path('', views.example_view, name='exapme'),
    path('variables/', views.variables_view, name='variables')
]