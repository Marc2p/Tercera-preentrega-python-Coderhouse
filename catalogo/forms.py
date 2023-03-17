from django import forms
from catalogo.models import *

class LibroForm(forms.ModelForm):
	class Meta:
		model = Libro
		fields = '__all__'

class AutorForm(forms.ModelForm):
	class Meta:
		model = Autor
		fields = '__all__'

class GeneroForm(forms.ModelForm):
	class Meta:
		model = Genero
		fields = '__all__'

class IdiomaForm(forms.ModelForm):
	class Meta:
		model = Idioma
		fields = '__all__'

class busquedaLibroForm(forms.Form):
	titulo = forms.CharField(label='Titulo', max_length=100, required=False)
	autor = forms.ModelChoiceField(label='Autor', queryset=Autor.objects.all(), required=False)
