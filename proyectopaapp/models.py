from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Proceso(models.Model):
	nombre = models.CharField(max_length = 50)
	tiempo = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
	capacidad = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
	def __str__(self):
		return self.nombre
	
class LineaDeProduccion(models.Model):
	nombre = models.CharField(max_length = 50)
	procesos = models.ManyToManyField(Proceso)

	def __str__(self):
		return self.nombre
	
class Producto(models.Model):
	nombre = models.CharField(max_length = 50)
	tiempoDeEntrada = models.DateTimeField()
