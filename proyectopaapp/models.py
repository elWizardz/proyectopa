from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Proceso(models.Model):
	nombre = models.CharField(max_length = 50)
	tiempo = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
	
class LineaDeProduccion(models.Model):
	nombre = models.CharField(max_length = 50)
	capacidad = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
	
class Producto(models.Model):
	nombre = models.CharField(max_length = 50)
	tiempoDeEntrada = models.DateTimeField()