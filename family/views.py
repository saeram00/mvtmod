from django.shortcuts import render
from .models import Relative


def family(request):
    fam_context = {
        'title': 'Family',
        'relatives': Relative.objects.all()
    }
    return render(request, 'family/base.html', fam_context)
