#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import tiempo
import datos
import algoritmo

#CAMBIAR "OPCION" POR 0 (Mejor viaje) o 1 (Segundo mejor viaje)
opcion = 0

class Viaje:
	def __init__(self, a, b):
		self.e1 = a
		self.e2 = b
		self.ls1 = datos.buscar_estacion(self.e1)
		self.ls2 = datos.buscar_estacion(self.e2)
		self.time = []
		self.pasos = []

def main():
	viaje = Viaje('Division del Norte', 'Salto del Agua')
	viaje = algoritmo.elegir_algoritmo(viaje)

	if len(viaje.pasos) < 1:
		print("Error: Ruta no encontrada")
		sys.exit(0)
	elif viaje.e1 == viaje.e2:
		print("Es la misma estacion")
		sys.exit(0)

	tiempo.imprimir_minutos(viaje.time[opcion])
	algoritmo.instrucciones(viaje.pasos[opcion])

"""
	A mejorar:
	
"""


if __name__ == '__main__':
	main()

