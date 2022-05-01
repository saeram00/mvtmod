from django.shortcuts import render
from .models import Book
from .forms import BookForm

# Create your views here.
def books(request):
    books_context = {
    'title': "Libros",
    'books': Book.objects.all(),
    }
    return render(request, 'books/base.html', books_context)
