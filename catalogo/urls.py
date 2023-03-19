from django.urls import path
from catalogo.views import *

urlpatterns = [
    path('', index, name="index"), # Vista de inicio
    path('libros/', libros, name="libros"), # Vista general de libros
    path('libros/<int:id>', libro, name="libro"), # Vista de un libro en particular
    path('BuscarLibro', busqueda_libro, name="BuscarLibro"), # Vista de búsqueda de libros
    path('agregarLibro', agregar_libro, name="agregar_libro"),
    path('autores', autores, name="autores"),
    path('autor/<int:id>', autor, name="autor"),
    path('agregarAutor', agregar_autor, name="agregar_autor"),
    path('agregarIdioma', agregar_idioma, name="agregar_idioma"),
    path('agregarGenero', agregar_genero, name="agregar_genero"),
]
