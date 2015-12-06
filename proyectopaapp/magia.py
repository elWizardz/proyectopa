from collections import deque
from threading import Timer
import json
from proyectopaapp.models import Proceso

procesos = {}

class ProcesoMagia:
	def __init__(self, id, tiempo, capacidad):
		self.id = id
		self.tiempo = tiempo * 60
		self.capacidad = capacidad
		self.corriendo = deque()
		self.espera = deque()

	def agregar(self, instancia):
		print("se agrego " + str(instancia))
		if len(self.corriendo) < self.capacidad:
			self.corriendo.append(instancia)
			Timer(1.0 * self.tiempo, self.moveProcess).start()

		else:
			self.espera.append(instancia)

	def moveProcess(self):
		instancia = self.corriendo.popleft()
		pendientes = json.loads(instancia.lista_pendientes)
		pendientes.pop(0)
		if len(pendientes) > 0:
			instancia.proceso = Proceso.objects.filter(id=pendientes[0])[0]
			instancia.lista_pendientes = json.dumps(pendientes)
			instancia.save()
			procesos[pendientes[0]].agregar(instancia)
		else:
			print("TERMINADO!" + str(instancia))
			instancia.terminado = True
			instancia.save()
		if len(self.espera) > 0:
			self.corriendo.append(self.espera.popleft())
			Timer(1.0 * self.tiempo, self.moveProcess).start()

for proc in Proceso.objects.all():
	procesos[proc.id] = ProcesoMagia(proc.id, proc.tiempo, proc.capacidad)

def agregarProceso(proc):
	procesos[proc.id] = ProcesoMagia(proc.id, proc.tiempo, proc.capacidad)
