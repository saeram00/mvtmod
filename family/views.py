from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Relative


rel1 = Relative(name="Robert House", age=38, birth=(1984, 12, 22))
rel2 = Relative(name="Maria Lockhart", age=22, birth=(2000, 4, 7))
rel3 = Relative(name="Loise Arzulo", age=28, birth=(1994, 7, 15))

relatives = (rel1, rel2, rel3)

fam_context = {
    'title': 'Family',
    'relatives': relatives
}

def family(request):
    return render(request, 'family/base.html', fam_context)
