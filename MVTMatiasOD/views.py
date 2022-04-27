from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html', {'title': 'Home', 'call_to_action': True})

