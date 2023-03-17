from django.contrib import admin
from catalogo.models import Genero, Idioma, Libro, Autor

# Register your models here.
admin.site.register(Genero)
admin.site.register(Idioma)
admin.site.register(Libro)
admin.site.register(Autor)