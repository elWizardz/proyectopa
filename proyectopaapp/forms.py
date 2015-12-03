from django import forms
from proyectopaapp.models import Proceso, LineaDeProduccion, Producto

class ProcesoForm(forms.ModelForm):
	class Meta:
		model = Proceso
		fields = ['nombre', 'tiempo', 'capacidad']
		error_messages = {
			'nombre' : {
				'required' : 'Indique el nombre del proceso',
			},
			'tiempo' : {
				'required' : 'Indique el tiempo requerido por el proceso',
				'invalid' : 'Tiempo invalido',
				'max_value' : 'Límite de tiempo excedido (MAX = 999)',
				'min_value' : 'Tiempo debe ser mayor a 0',
			},
			'capacidad' : {
        			'required' : 'Indique la capacidad del proceso',
				'invalid' : 'capacidad invalida',
				'max_value' : 'Limite de capacidad excedida (MAX = 999)',
				'min_value' : 'Capacidad debe ser mayor a 0',
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
		fields = ['nombre', 'cantidad', 'lineaDeProduccion']
		error_messages = {
			'nombre' : {
				'required' : 'Indique el nombre del proceso',
			},
			'cantidad' : {
				'required' : 'Indique la cantidad de productos',
				'invalid' : 'Cantidad invalida',
			},
			#TODO
			'lineaDeProduccion' : {
				'required' : 'Indique la linea de produccion',
				'invalid' : 'no es una linea de produccion valida',

			}
		}
