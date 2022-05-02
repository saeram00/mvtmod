from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books-index'),
    path('books-input/', views.book_input, name='books-input'),
    path('books-search/', views.search, name='books-search'),
]

