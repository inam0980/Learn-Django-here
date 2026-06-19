from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clothes/', views.clothes, name='clothes1'),
    path('fruits/', views.fruits, name='fruits1'),
]
