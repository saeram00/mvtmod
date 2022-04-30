from django import forms

class RelativeForm(forms.Form):

   nombre = forms.CharField(max_length=40) 
   edad = forms.IntegerField()
   nacimiento = forms.DateField()
   ocupacion = forms.CharField(max_length=50)

