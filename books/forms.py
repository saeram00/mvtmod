from django import forms


class BookForm(forms.Form):

    titulo_libro = forms.CharField(max_length=60)
    autor = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=20)
    publicacion = forms.IntegerField()

