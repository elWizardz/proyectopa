from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from proyectopaapp.models import Proceso, LineaDeProduccion, Producto, Instancia
from proyectopaapp.forms import ProcesoForm, LineaDeProduccionForm, ProductoForm

# Create your views here.

def index(request):
	return render_to_response("base.html", context_instance = RequestContext(request))

'''
###########################################
####		   P R O C E S O S         ####
###########################################
'''

def procesos(request):
	proceso = Proceso.objects.all()
	procesoForm = ProcesoForm()
	return render_to_response("procesos.html", {"proceso": proceso, "procesoForm": procesoForm}, context_instance = RequestContext(request))

def procesosAgregar(request):
	if request.method == 'POST':
		procesoForm = ProcesoForm(request.POST)
		if procesoForm.is_valid():
			procesoForm.save()
			procesoForm = ProcesoForm()
			message = "El proceso se ha agregado exitosamente."
			return render_to_response("procesos_agregar.html", {"procesoForm": procesoForm, "isAction": True, "isSuccess": True, "message": message}, context_instance = RequestContext(request))
		else:
			message = "No se pudo agregar el proceso."
			return render_to_response("procesos_agregar.html", {"procesoForm": procesoForm, "isAction": True, "isSuccess": False, "message": message}, context_instance = RequestContext(request))
	else:
		procesoForm = ProcesoForm()
		return render_to_response("procesos_agregar.html", {"procesoForm": procesoForm, "isAction": False}, context_instance = RequestContext(request))

def procesosEditar(request, proceso):
	if request.method == 'POST':
		procesoForm = ProcesoForm(request.POST)
		if procesoForm.is_valid():
			proceso = Proceso.objects.get(id = proceso)
			proceso.nombre = request.POST['nombre']
			proceso.tiempo = request.POST['tiempo']
			proceso.capacidad = request.POST['capacidad']
			proceso.save()
			procesoForm = ProcesoForm()
			message = "Los cambios han sido guardados."
			return render_to_response("procesos_editar.html", {"proceso": proceso, "procesoForm": procesoForm, "isAction": True, "isSuccess": True, "message": message}, context_instance = RequestContext(request))
		else:
			proceso = Proceso.objects.get(id = proceso)
			message = "No se pudo guardar los cambios."
			return render_to_response("procesos_editar.html", {"proceso": proceso, "procesoForm": procesoForm, "isAction": True, "isSuccess": False, "message": message}, context_instance = RequestContext(request))
	else:
		procesoForm = ProcesoForm()
		proceso = Proceso.objects.get(id = proceso)
		return render_to_response("procesos_editar.html", {"proceso": proceso, "procesoForm": procesoForm, "isAction": False}, context_instance = RequestContext(request))

def procesosBorrar(request, proceso):
	if request.method == 'POST':
		proceso = Proceso.objects.get(id = proceso)
		proceso.delete()
		return redirect("procesos")
	else:
		proceso = Proceso.objects.get(id = proceso)
		return render_to_response("procesos_borrar.html", {"proceso": proceso}, context_instance = RequestContext(request))

'''
######################################################
####     L I N E A S  D E  P R O D U C C I O N    ####
######################################################
'''

def lineasdeproduccion(request):
	lineadeproduccion = LineaDeProduccion.objects.all()
	lineaDeProduccionForm = LineaDeProduccionForm()
	return render_to_response("lineasdeproduccion.html", {"lineadeproduccion": lineadeproduccion, "lineaDeProduccionForm": lineaDeProduccionForm}, context_instance = RequestContext(request))

def lineasdeproduccionAgregar(request):
	if request.method == 'POST':
		lineaDeProduccionForm = LineaDeProduccionForm(request.POST)
		if lineaDeProduccionForm.is_valid():
			lineaDeProduccionForm.save()
			lineaDeProduccionForm = LineaDeProduccionForm()
			message = "La línea de producción se ha agregado exitosamente."
			return render_to_response("lineasdeproduccion_agregar.html", {"lineaDeProduccionForm": lineaDeProduccionForm, "isAction": True, "isSuccess": True, "message": message}, context_instance = RequestContext(request))
		else:
			message = "No se pudo agregar la línea de producción."
			return render_to_response("lineasdeproduccion_agregar.html", {"lineaDeProduccionForm": lineaDeProduccionForm, "isAction": True, "isSuccess": False, "message": message}, context_instance = RequestContext(request))
	else:
		lineaDeProduccionForm = LineaDeProduccionForm()
		return render_to_response("lineasdeproduccion_agregar.html", {"lineaDeProduccionForm": lineaDeProduccionForm, "isAction": False}, context_instance = RequestContext(request))

def lineasdeproduccionEditar(request, lineadeproduccion):
	if request.method == 'POST':
		lineaDeProduccionForm = LineaDeProduccionForm(request.POST)
		if lineaDeProduccionForm.is_valid():
			lineadeproduccion = LineaDeProduccion.objects.get(id = lineadeproduccion)
			lineadeproduccion.nombre = request.POST['nombre']
			lineadeproduccion.tiempo = request.POST['capacidad']
			lineadeproduccion.save()
			lineaDeProduccionForm = LineaDeProduccionForm()
			message = "Los cambios han sido guardados."
			return render_to_response("lineasdeproduccion_editar.html", {"lineadeproduccion": lineadeproduccion, "lineaDeProduccionForm": lineaDeProduccionForm, "isAction": True, "isSuccess": True, "message": message}, context_instance = RequestContext(request))
		else:
			lineadeproduccion = LineaDeProduccion.objects.get(id = lineadeproduccion)
			message = "No se pudo guardar los cambios."
			return render_to_response("lineasdeproduccion_editar.html", {"lineadeproduccion": lineadeproduccion, "lineaDeProduccionForm": lineaDeProduccionForm, "isAction": True, "isSuccess": False, "message": message}, context_instance = RequestContext(request))
	else:
		lineaDeProduccionForm = LineaDeProduccionForm()
		lineadeproduccion = LineaDeProduccion.objects.get(id = lineadeproduccion)
		return render_to_response("lineasdeproduccion_editar.html", {"lineadeproduccion": lineadeproduccion, "lineaDeProduccionForm": lineaDeProduccionForm, "isAction": False}, context_instance = RequestContext(request))

def lineasdeproduccionBorrar(request, lineadeproduccion):
	if request.method == 'POST':
		lineadeproduccion = LineaDeProduccion.objects.get(id = lineadeproduccion)
		lineadeproduccion.delete()
		return redirect("lineasdeproduccion")
	else:
		lineadeproduccion = LineaDeProduccion.objects.get(id = lineadeproduccion)
		return render_to_response("lineasdeproduccion_borrar.html", {"lineadeproduccion": lineadeproduccion}, context_instance = RequestContext(request))

'''
#############################################
####	      P R O D U C T O S          ####
#############################################
'''

def productos(request):
	producto = Producto.objects.all()
	productoForm = ProductoForm()
	return render_to_response("productos.html", {"producto": producto, "productoForm": productoForm}, context_instance = RequestContext(request))

def productosAgregar(request):
	if request.method == 'POST':
		productoForm = ProductoForm(request.POST)
		if productoForm.is_valid():
			producto = productoForm.save()
			proceso = producto.lineaDeProduccion.procesos.all()[0]
			for x in range(producto.cantidad):
				instancia = Instancia(producto = producto, proceso = proceso)
				instancia.save()
				print(x)
			productoForm = ProductoForm()
			message = "El producto se ha agregado exitosamente."
			return render_to_response("productos_agregar.html", {"productoForm": productoForm, "isAction": True, "isSuccess": True, "message": message}, context_instance = RequestContext(request))
		else:
			message = "No se pudo agregar el producto."
			return render_to_response("productos_agregar.html", {"productoForm": productoForm, "isAction": True, "isSuccess": False, "message": message}, context_instance = RequestContext(request))
	else:
		productoForm = ProductoForm()
		return render_to_response("productos_agregar.html", {"productoForm": productoForm, "isAction": False}, context_instance = RequestContext(request))

def productosEditar(request, producto):
	if request.method == 'POST':
		productoForm = ProductoForm(request.POST)
		if productoForm.is_valid():
			producto = Producto.objects.get(id = producto)
			producto.nombre = request.POST['nombre']
			producto.cantidad = request.POST['cantidad']
			producto.lineaDeProduccion = request.POST['lineaDeProduccion']
			producto.save()
			productoForm = ProductoForm()
			message = "Los cambios han sido guardados."
			return render_to_response("productos_editar.html", {"producto": producto, "productoForm": productoForm, "isAction": True, "isSuccess": True, "message": message}, context_instance = RequestContext(request))
		else:
			producto = Producto.objects.get(id = producto)
			message = "No se pudo guardar los cambios."
			return render_to_response("productos_editar.html", {"producto": producto, "productoForm": productoForm, "isAction": True, "isSuccess": False, "message": message}, context_instance = RequestContext(request))
	else:
		productoForm = ProductoForm()
		producto = Producto.objects.get(id = producto)
		return render_to_response("productos_editar.html", {"producto": producto, "productoForm": productoForm, "isAction": False}, context_instance = RequestContext(request))

def productosBorrar(request, producto):
	if request.method == 'POST':
		producto = Producto.objects.get(id = producto)
		producto.delete()
		return redirect("productos")
	else:
		producto = Producto.objects.get(id = producto)
		return render_to_response("productos_borrar.html", {"producto": producto}, context_instance = RequestContext(request))
