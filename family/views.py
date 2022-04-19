from django.shortcuts import render
from .models import Relative


fam_context = {
    'title': 'Family',
    'relatives': Relative.objects.all()
}

def family(request):
    return render(request, 'family/base.html', fam_context)
