from django.shortcuts import render

# Create your views here.
def home(request):
    home_context = {
        'title': 'Home',
        'call_to_action': True,
    }
    return render(request, 'home/index.html', home_context)

