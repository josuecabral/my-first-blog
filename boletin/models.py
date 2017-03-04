from django.db import models
from django.utils import timezone



# Create your models here.


class Registrado(models.Model):
	nombre = models.CharField(max_length=120, blank = False, null=True)
	apellido = models.CharField(max_length=120, blank = False, null=True)
	dni = models.IntegerField(unique=True, blank = False, null=True)
	direccion = models.CharField(max_length=120, blank = False, null=True)
	provincia_choices = (
		('Cordoba', 'Cordoba'),
		('La Rioja', 'La Rioja'),
		('Misiones', 'Misiones'),
		('San Luis', 'San Luis'),
		('Otra provincia', 'Otra provincia'),
		)
	provincia = models.CharField(max_length= 120, blank = False, null=True, choices= provincia_choices)
	fecha_nacimiento = models.DateField(default=timezone.now)
	iniciado = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado =models.DateTimeField(auto_now_add=False, auto_now=True)

	def __srt__(self): 
		return self.nombre