from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.predict, name='predict'),
    path('result/', views.result, name='result')

]
