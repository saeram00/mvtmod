from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestoForm

# Create your views here.
def restaurants(request):
    restaurants_context = {
    'title': 'Restaurants',
    'restaurants': Restaurant.objects.all(),
    }
    return render(request, 'restaurants/base.html', restaurants_context)

def restaurant_input(request):
    if request.method == 'POST':
        restaurant_form = RestoForm(request.POST) # Llega la info del HTML
        if restaurant_form.is_valid(): # Valida desde Django
            info = restaurant_form.cleaned_data # Almacena la info del form en un dict
            new_restaurant = Restaurant(resto_name=info['nombre_resto'],
                             category=info['categoria'],
                             stars=info['estrellas'],
                             reservation=info['reservas'],
                             )
            new_restaurant.save()
            return redirect('restaurants-index') # Te envía a una página escogida al enviar el form
    else:
        restaurant_form = RestoForm() # Form vacío al cargar el HTML

    restaurant_input_context = {
        'title': 'Restaurants',
        'restaurant_form': restaurant_form,
    }

    return render(request, 'restaurants/restaurant_input.html', restaurant_input_context)

def search(request):
    if request.GET.get('query-resto'):
        resto_name_q = request.GET.get('query-resto')
        resto_search = Restaurant.objects.filter(resto_name__icontains=resto_name_q)
        return render(request, 'restaurants/results.html',
                      {'results': resto_search, 'title': 'Restaurants'}
                      )

    return render(request, 'restaurants/search.html', {'title': 'Restaurants'})
