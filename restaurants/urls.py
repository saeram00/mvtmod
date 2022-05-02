from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurants, name='restaurants-index'),
    path('restaurants-input/', views.restaurant_input, name='restaurants-input'),
    path('restaurants-search/', views.search, name='restaurants-search'),
]

