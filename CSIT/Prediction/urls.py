from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.prediction, name='prediction'),
    path('result/', views.result, name='result')

]
