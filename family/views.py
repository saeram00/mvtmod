from django.shortcuts import render, redirect
from .models import Relative
from .forms import RelativeForm


def family(request):
    fam_context = {
        'title': 'Family',
        'relatives': Relative.objects.all(),
    }

    return render(request, 'family/base.html', fam_context)


def fam_input(request):
    if request.method == 'POST':
        rel_form = RelativeForm(request.POST) # Llega la info del HTML
        if rel_form.is_valid(): # Valida desde Django
            info = rel_form.cleaned_data # Almacena la info del form en un dict
            new_rel = Relative(name=info['nombre'],
                               age=info['edad'],
                               birth=info['nacimiento'],
                               job=info['ocupacion']
                               )
            new_rel.save()
            return redirect('family-tree') # Te envía a una página escogida al enviar el form
    else:
        rel_form = RelativeForm() # Form vacío al cargar el HTML

    fam_input_context = {
        'rel_form': rel_form,
    }

    return render(request, 'family/fam_input.html', fam_input_context)

def fam_edit(request):
    if request.method == 'POST':
        rel_form = RelativeForm(request.POST) # Llega la info del HTML
        if rel_form.is_valid(): # Valida desde Django
            info = rel_form.cleaned_data # Almacena la info del form en un dict
            new_rel = Relative(name=info['nombre'],
                               age=info['edad'],
                               birth=info['nacimiento'],
                               job=info['ocupacion']
                               )
            new_rel.save()
            return render(request, 'family/base.html') # Te envía a una página escogida al enviar el form
    else:
        rel_form = RelativeForm() # Form vacío al cargar el HTML

    fam_edit_context = {
        'rel_form': rel_form,
    }

    return render(request, 'family/fam_edit.html', fam_edit_context)

def fam_delete(request):
    if request.method == 'POST':
        rel_form = RelativeForm(request.POST) # Llega la info del HTML
        if rel_form.is_valid(): # Valida desde Django
            info = rel_form.cleaned_data # Almacena la info del form en un dict
            new_rel = Relative(name=info['nombre'],
                               age=info['edad'],
                               birth=info['nacimiento'],
                               job=info['ocupacion']
                               )
            new_rel.save()
            return render(request, 'family/base.html') # Te envía a una página escogida al enviar el form
    else:
        rel_form = RelativeForm() # Form vacío al cargar el HTML

    fam_delete_context = {
        'rel_form': rel_form,
    }

    return render(request, 'family/fam_delete.html', fam_delete_context)

