from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from catalogo.forms import *
from catalogo.models import *

# Create your views here.

def context_processor(request):
	ctx = {'buscar_libro': busquedaLibroForm(prefix='busqueda')}
	return ctx

def index(request): # Vista de inicio
		cantidad_de_libros = Libro.objects.all().count()
		cantidad_de_autores = Autor.objects.count()

		ctx = {
			'cantidad_de_libros': cantidad_de_libros,
			'cantidad_de_autores': cantidad_de_autores,
			# 'buscar_libro': busquedaLibroForm(),
		}

		return render(request, 'index.html', ctx)

def libros(request): # Vista general de libros
		libros = Libro.objects.all().order_by('titulo')
		paginator = Paginator(libros, 10)
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
		ctx = {'paginador': autores}

		return render(request, 'autores.html', ctx)

def autor(request, id): # Vista de libros de un autor en particular
		autor = Autor.objects.get(id=id)
		libros = Libro.objects.filter(autor=autor).order_by('titulo')
		paginator = Paginator(libros, 10)
		page = request.GET.get('page')
		libros = paginator.get_page(page)

		ctx = {'autor': autor, 'paginador': libros}
		return render(request, 'libros_autor.html', ctx)

def busqueda_libro(request): # Vista de busqueda de libros
		form = busquedaLibroForm(request.GET, prefix='busqueda')
		if form.is_valid():
			data = form.cleaned_data
			libros = Libro.objects.all()
			if data['titulo']:
				libros = Libro.objects.filter(titulo__icontains=data['titulo']).order_by('titulo')
			if data['autor']:
				libros = libros.filter(autor=data['autor']).order_by('titulo')
			paginator = Paginator(libros, 10)
			page = request.GET.get('page')
			libros = paginator.get_page(page)
			ctx = {'paginador': libros}
			return render(request, 'libros.html', ctx)

def agregar_libro(request): # Vista de agregar un libro
		if request.method == 'POST':
			form = LibroForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data
				nuevo_libro = Libro(
					titulo=data['titulo'],
					autor=data['autor'],
					idioma=data['idioma'],
					fecha_publicacion=data['fecha_publicacion'],
					sinopsis=data['sinopsis']
				)
				nuevo_libro.save()
				nuevo_libro.genero.set(data['genero'])
				return redirect('libros')
		ctx = {'form': LibroForm}
		return render(request, 'agregar_libro.html', ctx)

def agregar_autor(request): # Vista de agregar un autor
		if request.method == 'POST':
			form = AutorForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data
				nuevo_autor = Autor(
					nombre=data['nombre'],
					apellido=data['apellido'],
				)
				nuevo_autor.save()
				return redirect('autores')
		ctx = {'form': AutorForm}
		return render(request, 'agregar_autor.html', ctx)

def agregar_genero(request): # Vista de agregar un genero
		if request.method == 'POST':
			form = GeneroForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data
				nuevo_genero = Genero(
					nombre=data['nombre'],
				)
				nuevo_genero.save()
				return redirect('index')
		ctx = {'form': GeneroForm}
		return render(request, 'agregar_genero.html', ctx)

def agregar_idioma(request): # Vista de agregar un idioma
		if request.method == 'POST':
			form = IdiomaForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data
				nuevo_idioma = Idioma(
					nombre=data['nombre'],
				)
				nuevo_idioma.save()
				return redirect('index')
		ctx = {'form': IdiomaForm}
		return render(request, 'agregar_idioma.html', ctx)