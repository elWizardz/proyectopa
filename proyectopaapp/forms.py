from django import forms
from proyectopaapp.models import Proceso, LineaDeProduccion, Producto

class ProcesoForm(forms.ModelForm):
	class Meta:
		model = Proceso
		fields = ['nombre', 'tiempo']
		error_messages = {
			'nombre' : {
				'required' : 'Indique el nombre del proceso',
			},
			'tiempo' : {
				'required' : 'Indique el tiempo requerido por el proceso',
				'invalid' : 'Tiempo invalido',
				'max_value' : 'Límite de tiempo excedido (MAX = 999)',
				'min_value' : 'Tiempo debe ser mayor a 0',
			}
		}

class LineaDeProduccionForm(forms.ModelForm):
	class Meta:
		model = LineaDeProduccion
		fields = ['nombre', 'procesos']
		error_messages = {
			'nombre' : {
				'required' : 'Indique el nombre del proceso',
			},
                        #TODO
			'procesos' : {
			}
		}
		
class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = ['nombre', 'tiempoDeEntrada']
		error_messages = {
			'nombre' : {
				'required' : 'Indique el nombre del proceso',
			},
			'tiempoDeEntrada' : {
				'required' : 'Indique el tiempo requerido por el proceso',
				'invalid' : 'Tiempo invalido',
			}
		}
