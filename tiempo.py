#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	Aqui estan las funciones para calcular
	tiempos entre estaciones
"""

#Calcula el tiempo entre estaciones de su misma linea
def tiempo(e1, e2, linea):
	# (tp) Tiempo perdido && (t) tiempo
	tp = 15
	t = 0
	primera_estacion = None
	
	for estacion in linea:		
		if primera_estacion == None:
			if estacion[0] == e1 or estacion[0] == e2:
				primera_estacion = True
				
		elif estacion[0] == e1 or estacion[0] == e2:
			t = t + estacion[1]
			return t
		else:
			t = t + estacion[1] + tp
			
def tiempo_transborde(estacion):
	n = 180 #Tiempo promedio de llegada del metro a la estacion
	transborde = { 
					'Tacubaya': 310,
					'Balderas': 219,
					'Salto del Agua': 251,
					'Pino Suarez': 200,
					'Candelaria': 330,
					'San Lazaro': 376,
					'Pantitlan': 600,
					'Tacuba': 295,
					'Hidalgo': 108,
					'Bellas Artes': 300,
					'Chabacano': 402,
					'Deportivo 18 de Marzo': 316,
					'La Raza': 471,
					'Guerrero': 143,
					'Centro Medico': 241,
					'Martin Carrera': 497,
					'Consulado': 399,
					'Morelos': 184,
					'Jamaica': 395,
					'Santa Anita': 274,
					'Oceania': 134,
					'Instituto del Petroleo': 418,
					'El Rosario': 100,
					'Garibaldi': 183

				} 
					
	if estacion in transborde:
		return transborde[estacion]+n
	else:
		return 0
		
#Pasa el tiempo de segundos a formato MM:SS
def imprimir_minutos(t_seg):
	t_min = [0,0]
	while(t_seg > 60):
		t_seg = t_seg - 60
		t_min[0] = t_min[0] + 1
	t_min[1] = t_seg
	if t_min[1] >= 30:
		t_min[0] += 1

	print "Tiempo aproximado: " + str(t_min[0]) + " minutos.\n"
