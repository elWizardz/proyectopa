from django.conf.urls import include, url
from django.contrib import admin
from proyectopaapp import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	
	url(r'^procesos/$', views.procesos, name="procesos"),
	url(r'^procesos/agregar/$', views.procesosAgregar),
	url(r'^procesos/editar/(?P<proceso>([0-9]+))/$', views.procesosEditar),
	url(r'^procesos/borrar/(?P<proceso>([0-9]+))/$', views.procesosBorrar),
	
	url(r'^lineasdeproduccion/$', views.lineasdeproduccion, name="lineasdeproduccion"),
	url(r'^lineasdeproduccion/agregar/$', views.lineasdeproduccionAgregar),
	url(r'^lineasdeproduccion/editar/(?P<lineadeproduccion>([0-9]+))/$', views.lineasdeproduccionEditar),
	url(r'^lineasdeproduccion/borrar/(?P<lineadeproduccion>([0-9]+))/$', views.lineasdeproduccionBorrar),
	
	url(r'^productos/$', views.productos, name="productos"),
	url(r'^productos/agregar/$', views.productosAgregar),
	url(r'^productos/editar/(?P<producto>([0-9]+))/$', views.productosEditar),
	url(r'^productos/borrar/(?P<producto>([0-9]+))/$', views.productosBorrar),
	
	url(r'^assets/res/(?P<path>.*)/$', 'django.views.static.serve',
        {'document_root': 'proyectopaapp/assets/res'}),
	url(r'^assets/css/(?P<path>.*)/$', 'django.views.static.serve',
        {'document_root': 'proyectopaapp/assets/css'}),
	url(r'^assets/js/(?P<path>.*)/$', 'django.views.static.serve',
        {'document_root': 'proyectopaapp/assets/js'}),
	url(r'^assets/fonts/(?P<path>.*)/$', 'django.views.static.serve',
        {'document_root': 'proyectopaapp/assets/fonts'}),
]