from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from catalogo.forms import *
from catalogo.models import *

# Create your views here.
def index(request): # Vista de inicio
		cantidad_de_libros = Libro.objects.all().count()
		cantidad_de_autores = Autor.objects.count()

		ctx = {
			'cantidad_de_libros': cantidad_de_libros,
			'cantidad_de_autores': cantidad_de_autores,
			'buscar_libro': busquedaLibroForm(),
		}

		return render(request, 'index.html', ctx)

def libros(request): # Vista general de libros
		libros = Libro.objects.all().order_by('titulo')
		paginator = Paginator(libros, 2)
		page = request.GET.get('page')
		libros = paginator.get_page(page)
		ctx = {'paginador': libros}

		return render(request, 'libros.html', ctx)

def libro(request, id): # Vista de un libro en particular
		libro = Libro.objects.get(id=id)
		ctx = {'libro': libro}
		return render(request, 'libro.html', ctx)

def autores(request): # Vista general de autores
		autores = Autor.objects.all().order_by('nombre')
		paginator = Paginator(autores, 10)
		page = request.GET.get('page')
		autores = paginator.get_page(page)
		print(autores)
		ctx = {'paginador': autores}

		return render(request, 'autores.html', ctx)

def autor(request, id): # Vista de libros de un autor en particular
		autor = Autor.objects.get(id=id)
		libros = Libro.objects.filter(autor=autor).order_by('titulo')
		paginator = Paginator(libros, 2)
		page = request.GET.get('page')
		libros = paginator.get_page(page)

		ctx = {'autor': autor, 'paginador': libros}
		return render(request, 'libros_autor.html', ctx)

def busqueda_libro(request): # Vista de busqueda de libros
		form = busquedaLibroForm(request.GET)
		if form.is_valid():
			data = form.cleaned_data
			libros = Libro.objects.all()
			if data['titulo']:
				libros = Libro.objects.filter(titulo__icontains=data['titulo']).order_by('titulo')
			if data['autor']:
				libros = libros.filter(autor=data['autor']).order_by('titulo')
			paginator = Paginator(libros, 2)
			page = request.GET.get('page')
			libros = paginator.get_page(page)
			ctx = {'paginador': libros}
			return render(request, 'libros.html', ctx)
		