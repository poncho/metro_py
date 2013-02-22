#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datos
import tiempo
import metro

"""
	Aqui estan los algoritmos
	para el programa del metro
"""

#Se relizan las pruebas de algoritmos
def elegir_algoritmo(viaje):
	#v es True si el algoritmo funciona
	v = False

	if [12] == viaje.ls1 and [10] == viaje.ls2:
		est_final, viaje.e2 = viaje.e2, "Pantitlan"
		viaje.ls2 = [1, 5, 9] #Se cambian por las lineas de Pantitlan
		viaje = tres_transbordes(viaje, est_final)
		return viaje
	elif [12] == viaje.ls2 and [10] == viaje.ls1:
		est_final, viaje.e1 = viaje.e1, "Pantitlan"
		viaje.ls1 = [1, 5, 9]
		viaje = tres_transbordes(viaje, est_final)
		return viaje


	v, viaje = misma_linea(viaje)

	if v == False:
		v, viaje = un_transborde(viaje)

	if v == False:
		v, viaje = dos_transbordes(viaje)
	else:
		temp = metro.Viaje(viaje.e1, viaje.e2)
		v, temp = dos_transbordes(temp)
		if temp.pasos != []:
			viaje.pasos = integrar_todo(viaje, temp)
			viaje.time, viaje.pasos = mejores_opciones(viaje.pasos)
		else:
			viaje.time = [viaje.time]
			viaje.pasos = [viaje.pasos]

		
	return viaje

	 
#Algoritmo 0 : Misma linea las estaciones
def misma_linea(viaje):
	for linea in viaje.ls1:
		if linea in viaje.ls2:
			l = datos.obtener_linea(linea)
			viaje.pasos = [viaje.e1, direccion(viaje.e1, viaje.e2, l), viaje.e2]
			viaje.time = tiempo.tiempo(viaje.e1, viaje.e2, l)
			return True, viaje

	return False, viaje
			
#Algoritmo 1: Un transborde
def un_transborde(viaje):
	for linea2 in viaje.ls2:
		l2 = datos.obtener_linea(linea2)
		for linea1 in viaje.ls1:
			l1 = datos.obtener_linea(linea1)
			for estacion in l2:
				if estacion[2] != None and linea1 in estacion[2]:
					viaje.time = tiempo.tiempo(viaje.e1, estacion[0], datos.obtener_linea(linea1))
					viaje.time = viaje.time + tiempo.tiempo(viaje.e2, estacion[0], l2)
					viaje.time = viaje.time + tiempo.tiempo_transborde(estacion[0])
					viaje.pasos.append([viaje.time, viaje.e1, linea1, estacion[0], linea2, viaje.e2])

	if len(viaje.pasos) >= 1:
		viaje.time, viaje.pasos = mejores_opciones(viaje.pasos)
		viaje.pasos = acomodar_opciones(viaje.pasos, 4)
		return True, viaje

	return False, viaje
	
#Algoritmo 2: Dos transbordes
def dos_transbordes(viaje):
	lc = []
	posibles_transbordes = []

	for linea1 in viaje.ls1:
		l1 = datos.obtener_linea(linea1)
		for linea2 in viaje.ls2:
			l2 = datos.obtener_linea(linea2)
			lc = lineas_comunes(l1, l2)
			for lineacomun in lc:
				viaje.time = 0

				#Encuentra transborde1 y mide el tiempo entre e1 y transborde1
				transb_1 = existe_transborde(linea1, lineacomun)
				if transb_1 == viaje.e1:
					continue
				viaje.time += tiempo.tiempo(viaje.e1, transb_1, l1)
				viaje.time += tiempo.tiempo_transborde(transb_1)

				#Encuentra transborde2 y mide el tiempo entre transborde1 y transborde2
				transb_2 = existe_transborde(linea2, lineacomun)
				if transb_2 == transb_1 or transb_2 == viaje.e2:
					continue
				viaje.time += tiempo.tiempo(transb_1, transb_2, datos.obtener_linea(lineacomun))
				viaje.time += tiempo.tiempo_transborde(transb_2)

				#Mide el tiempo entre transborde2 y e2
				viaje.time += tiempo.tiempo(transb_2, viaje.e2, l2)

				#Agrega los recorridos a una lista de posibles transbordes
				viaje.pasos.append([viaje.time, viaje.e1, linea1, transb_1, lineacomun, transb_2, linea2, viaje.e2])

	if len(viaje.pasos) >= 1:
		viaje.time, viaje.pasos = mejores_opciones(viaje.pasos)
		#Cambia las lineas por las direcciones en el mejor recorrido
		viaje.pasos = acomodar_opciones(viaje.pasos, 6)
		return True, viaje
				
		
	return False, viaje

#Caso especial para un viaje de Linea 12 a Linea A
#Cuando ninguno de los dos es un transborde
def tres_transbordes(viaje, est_final):
	#Se hace el viaje de dos transbordes de la
	#estacion de la linea 12 a Pantitlan
	v, viaje = dos_transbordes(viaje)
	return viaje


def existe_transborde(linea1, linea2):
	l2 = datos.obtener_linea(linea2)
	for estacion in l2:
		if estacion[2] != None:
			if linea1 in estacion[2]:
				return estacion[0]
				
	#Checa si existe un transborde entre el punto final y el primer transborde
	#y revisa si es línea en comun con el punto inicial
	
	return None

	
#Busca alguna(s) linea(s) en comun de dos lineas
def lineas_comunes(l1, l2):
	temp = []
	l_comunes = []
	#Toma todas las estaciones que transbordan con l1 y las guarda en temp
	for estacion in l1:
		if estacion[2] != None:
			for t in estacion[2]:
				if t not in temp:
					temp.append(t)
	#Revisa si las estaciones que transbordan en l2 estan en temp y las
	#agrega a la lista final
	for estacion in l2:
		if estacion[2] != None:
			for t in estacion[2]:
				if t in temp and t not in l_comunes:
					l_comunes.append(t)
	
	return l_comunes
	
#Obtiene la dirección a la que se tiene que tomar el metro
def direccion(e1, e2, linea):
	for estacion in linea:
		if estacion[0] == e1:
			dir = linea[-1][0]
			return dir
		elif estacion[0] == e2:
			dir = linea[0][0]
			return dir

def mejores_opciones(opciones):
	mejores_opciones = []
	tiempos = []

	#Para casos transborde unico
	if len(opciones) == 1:
		return [opciones[0][0]], [opciones[0][1:]]

	#Acomoda los dos mejores tiempos
	for recorrido in opciones:
		if mejores_opciones == []:
			mejores_opciones.append(recorrido)
		elif recorrido[0] < mejores_opciones[0][0]:
			mejores_opciones.append(mejores_opciones[0])
			mejores_opciones[0] = recorrido
			if mejores_opciones[-1][0] < mejores_opciones[-2][0]:
				mejores_opciones[1] = mejores_opciones.pop()
		elif len(mejores_opciones) == 1:
			mejores_opciones.append(recorrido)
		elif recorrido[0] < mejores_opciones[1][0]:
			mejores_opciones[1] = recorrido

	#Separa los tiempos y los recorridos
	for recorrido in mejores_opciones:
		tiempos.append(recorrido.pop(0))
		recorrido = recorrido[1:]

	return tiempos, mejores_opciones

#Obtiene el mejor recorrido de una lista de ellos.
def mejor_recorrido(pasos):
	mejor_rec = []

	#Para casos de un transborde únicos
	if len(pasos) == 1:
		return pasos[0][0], pasos[0][1:]
		
	for recorrido in pasos:
		if mejor_rec == []:
			mejor_rec = recorrido
		elif recorrido[0] < mejor_rec[0]:
			mejor_rec = recorrido

	return mejor_rec[0], mejor_rec[1:]

#Deja las opciones de recorridos listos para imprimirse
def acomodar_opciones(opciones, n):
	for opcion in opciones:
		for i in range(1, n, 2):
			opcion[i] = direccion(opcion[i-1], opcion[i+1], datos.obtener_linea(opcion[i]))

	return opciones

#Junta los viajes de un transborde con los de dos y crea un array.
def integrar_todo(viaje1, viaje2):
	opciones = []

	#Se pasa todo lo de viaje1 a viaje2
	for tiempo in viaje1.time:
		viaje2.time.append(tiempo)
	for paso in viaje1.pasos:
		viaje2.pasos.append(paso)

	for i in range(len(viaje2.time)):
		opciones.append([viaje2.time[i]])
		for dato in viaje2.pasos[i]:
			opciones[i].append(dato)

	return opciones

	
#Imprime las instrucciones del viaje en metro
def instrucciones(pasos):
	while len(pasos) > 0:
		print "De " + pasos[0]
		print "Con direccion " + pasos[1]
		print "Hasta " + pasos[2]
		print "\n"

		if len(pasos) > 3:
			pasos = pasos[2:]
		else:
			pasos = []
