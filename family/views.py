from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models

# Create your views here.
def test(request):
    return render(request, 'family/base.html', {'title': 'test title'})
