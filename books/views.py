from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def books(request):
    books_context = {
    'title': 'Libros',
    'books': Book.objects.all(),
    }
    return render(request, 'books/base.html', books_context)

def book_input(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST) # Llega la info del HTML
        if book_form.is_valid(): # Valida desde Django
            info = book_form.cleaned_data # Almacena la info del form en un dict
            new_book = Book(book_title=info['titulo_libro'],
                            author=info['autor'],
                            genre=info['genero'],
                            published=info['publicacion'],
                            book_length=info['paginas']
                            )
            new_book.save()
            return redirect('books-index') # Te envía a una página escogida al enviar el form
    else:
        book_form = BookForm() # Form vacío al cargar el HTML

    book_input_context = {
        'title': 'Libros',
        'book_form': book_form,
    }

    return render(request, 'books/book_input.html', book_input_context)

def search(request):
    if request.GET.get('query-title'):
        bk_title = request.GET.get('query-title')
        bk_search = Book.objects.filter(book_title__icontains=bk_title)
        return render(request, 'books/results.html',
                      {'results': bk_search, 'title': 'Libros'}
                      )

    return render(request, 'books/search.html', {'title': 'Libros'})
