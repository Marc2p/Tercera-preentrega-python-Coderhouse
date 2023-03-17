from django.db import models

# Create your models here.

class Genero(models.Model):
	nombre = models.CharField(max_length=150)

	def __str__(self):
		return self.nombre

class Idioma(models.Model):
	nombre = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre

class Libro(models.Model):
	titulo = models.CharField(max_length=150)
	autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
	idioma = models.ForeignKey('Idioma', on_delete=models.SET_NULL, null=True)
	fecha_publicacion = models.DateField()
	genero = models.ManyToManyField(Genero)
	sinopsis = models.TextField(max_length=1000)

	def __str__(self):
		return self.titulo

class Autor(models.Model):
	nombre = models.CharField(max_length=150)
	apellido = models.CharField(max_length=150)

	class Meta:
		verbose_name_plural = "Autores"

	def __str__(self):
		return f"{self.nombre} {self.apellido}"

	def get_libros(self):
		return Libro.objects.filter(autor=self)
