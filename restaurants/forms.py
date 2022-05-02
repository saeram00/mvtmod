from django import forms

class RestoForm(forms.Form):

    nombre_resto = forms.CharField(max_length=60)
    categoria = forms.CharField(max_length=50)
    estrellas = forms.IntegerField()
    reservas = forms.BooleanField()
