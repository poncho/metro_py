#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
	Aqui estan las bases de datos
	de los tiempos de las lineas
	del metro					
"""
def busca(e, LX):  #Busca la estación y su posición para cualquier línea
	i = 0
	for estacion in LX:
		if estacion[0] == e:
			if estacion[3] != None:
				return LX, estacion[3] #Caso de estacion en dos lineas
			return LX, None
		i += 1
	return None, None

def obtener_linea(n):
	# Tiempo en segundos
		#[1] Tiempo de Arriba para abajo [Prueba]
		#[2] Tiempo de Abajo para arriba [Prueba]

	if n == 1:
		return [['Observatorio', 0, None], 
				['Tacubaya', 108, [7,9]],
				['Juanacatlan', 100, None],
				['Chapultepec', 86, None],
				['Sevilla', 50, None],
				['Insurgentes', 61, None],
				['Cuauhtemoc', 72, None],
				['Balderas', 43, [3]],
				['Salto del Agua', 47, [8]],
				['Isabel la Catolica', 46, None],
				['Pino Suarez', 41, [2]],
				['Merced', 69, None],
				['Candelaria', 65, [4]],
				['San Lazaro', 78, [11]],
				['Moctezuma', 48, None],
				['Balbuena', 65, None],
				['Boulevard Puerto Aereo', 57, None],
				['Gomez Farias', 58, None],
				['Zaragoza', 70, None],
				['Pantitlan', 113, [5, 9, 10]]]
				
	elif n == 2:
		return [['Cuatro Caminos', 0, None],
				['Panteones', 164, None],
				['Tacuba', 144, [7]],
				['Cuitlahuac', 72, None],
				['Popotla', 71, None],
				['Colegio Militar', 56, None],
				['Normal', 61, None],
				['San Cosme', 74, None],
				['Revolucion', 63, None],
				['Hidalgo', 68, [3]],
				['Bellas Artes', 55, [8]],
				['Allende', 49, None],
				['Zocalo', 69, None],
				['Pino Suarez', 82, [1]],
				['San Antonio Abad', 89, None],
				['Chabacano', 73, [8, 9]],
				['Viaducto', 85, None],
				['Xola', 59, None],
				['Villa de Cortes', 78, None],
				['Nativitas', 83, None],
				['Portales', 98, None],
				['Ermita', 82, [12]],
				['General Anaya', 91, None],
				['Tasqueña', 136, None]]
	
	elif n == 3:
		return [['Indios Verdes', 0, None],
				['Deportivo 18 de Marzo', 117, [6]],
				['Potrero', 99, None],
				['La Raza', 112, [5]],
				['Tlatelolco', 142, None],
				['Guerrero', 106, [11]],
				['Hidalgo', 76, [2]],
				['Juarez', 36, None],
				['Balderas', 72, [1]],
				['Niños Heroes', 73, None],
				['Hospital General', 63, None],
				['Centro Medico', 71, [9]],
				['Etiopia', 113, None],
				['Eugenia', 98, None],
				['Division del Norte', 77, None],
				['Zapata', 84, [12]],
				['Coyoacan', 116, None],
				['Viveros', 94, None],
				['Miguel Angel de Quevedo', 87, None],
				['Copilco', 129, None],
				['Universidad', 130, None]]
		
	elif n == 4:
		return [['Martin Carrera', 0, [6]],
				['Talisman', 107, None],
				['Bondojito', 92, None],
				['Consulado', 66, [5]],
				['Canal del Norte', 86, None],
				['Morelos', 88, [11]],
				['Candelaria', 101, [1]],
				['Fray Servando', 65, None],
				['Jamaica', 99, [9]],
				['Santa Anita', 76, [8]]]
		
	elif n == 5:
		return [['Politecnico', 0, None],
				['Instituto del Petroleo', 116, [6]],
				['Autobuses del Norte', 105, None],
				['La Raza', 97, [3]],
				['Misterios', 90, None],
				['Valle Gomez', 97, None],
				['Consulado', 72, [4]],
				['Eduardo Molina', 84, None],
				['Aragon', 87, None],
				['Oceania', 119, [11]],
				['Terminal Aerea', 115, None],
				['Hangares', 113, None],
				['Pantitlan', 155, [1, 9, 10]]]
		
	elif n == 6:
		return [['El Rosario', 0, [7]],
				['Tezozomoc', 117, None],
				['Azcapotzalco', 94, None],
				['Ferreria', 110, None],
				['Norte 45', 102, None],
				['Vallejo', 68, None],
				['Instituto del Petroleo', 75, [5]],
				['Lindavista', 117, None],
				['Deportivo 18 de Marzo', 102, [3]],
				['La Villa-Basilica', 60, None],
				['Martin Carrera', 108, [4]]]
		
	elif n == 7:
		return [['El Rosario', 0, [6]],
				['Aquiles Serdan', 134, None],
				['Camarones', 118, None],
				['Refineria', 84, None],
				['Tacuba', 110, [2]],
				['San Joaquin', 120, None],
				['Polanco', 100, None],
				['Auditorio', 73, None],
				['Constituyentes', 120, None],
				['Tacubaya', 88, [1,9]],
				['San Pedro de los Pinos', 94, None],
				['San Antonio', 58, None],
				['Mixcoac', 71, [12]],
				['Barranca del Muerto', 124, None]]
			  
	elif n == 8:
		return [['Garibaldi', 0, [11]],
				['Bellas Artes', 65, [2]],
				['San Juan de Letran', 51, None],
				['Salto del Agua', 37, [1]],
				['Doctores', 60, None],
				['Obrera', 76, None],
				['Chabacano', 108, [2, 9]],
				['La Viga', 83, None],
				['Santa Anita', 65, [4]],
				['Coyuya', 93, None],
				['Iztacalco', 95, None],
				['Apatlaco', 88, None],
				['Aculco', 57, None],
				['Escuadron 201', 78, None],
				['Atlalilco', 157, [12]],
				['Iztapalapa', 74, None],
				['Cerro de la Estrella', 72, None],
				['UAM-I', 107, None],
				['Constitucion de 1917', 107, None]]
		
	elif n == 9:
		return [['Tacubaya', 0, [1, 7]], 
				['Patriotismo', 120, None],
				['Chilpancingo', 74, None],
				['Centro Medico', 99, [3]],
				['Lazaro Cardenas', 76, None],
				['Chabacano', 85, [2, 8]],
				['Jamaica', 92, [4]],
				['Mixiuhca', 90, None],
				['Velodromo', 95, None],
				['Ciudad Deportiva', 102, None],
				['Puebla', 86, None],
				['Pantitlan', 100, [1, 5, 10]]]
		
	elif n == 10:
		return [['Pantitlan', 0, [1, 5, 9]],
				['Agricola Oriental', 130, None],
				['Canal de San Juan', 104, None],
				['Tepalcates', 134, None],
				['Guelatao', 109, None],
				['Peñon Viejo', 196, None],
				['Acatitla', 127, None],
				['Santa Marta', 104, None],
				['Los Reyes', 161, None],
				['La Paz', 176, None]]
		
	elif n == 11:
		return [['Buenavista', 0, None],
				['Guerrero', 56, [3]],
				['Garibaldi', 76, [8]],
				['Lagunilla', 52, None],
				['Tepito', 64, None],
				['Morelos', 54, [4]],
				['San Lazaro', 121, [1]],
				['Flores Magon', 89, None],
				['Romero Rubio', 89, None],
				['Oceania', 81, [5]],
				['Deportivo Oceania', 85, None],
				['Bosque de Aragon', 110, None],
				['Villa de Aragon', 78, None],
				['Nezahualcoyotl', 125, None],
				['Impulsora', 130, None],
				['Rio de los Remedios', 49, None],
				['Muzquiz', 110, None],
				['Ecatepec', 137, None],
				['Olimpica', 63, None],
				['Plaza Aragon', 72, None],
				['Ciudad Azteca', 61, None]]
				
	elif n == 12:
		return [['Mixcoac', 0, [7]],
				['Insurgentes Sur', 0, None],
				['Hospital 20 de Noviembre', 0, None],
				['Zapata', 0, [3]],
				['Parque de los Venados', 0, None],
				['Eje Central', 0, None],
				['Ermita', 0, [2]],
				['Mexicaltzingo', 0, None],
				['Atlalilco', 0, [8]],
				['Culhuacan', 0, None],
				['San Andres Tomatlan', 0, None],
				['Lomas Estrella', 0, None],
				['Calle 11', 0, None],
				['Periferico Oriente', 0, None],
				['Tezonco', 0, None],
				['Olivos', 0, None],
				['Nopalera', 0, None],
				['Zapotitlan', 0, None],
				['Tlaltengo', 0, None],
				['Tlahuac', 0, None]]
		
			
def buscar_estacion(e):
		
	estaciones = {
		'Observatorio': [1],
		'Tacubaya': [1, 7, 9],
		'Juanacatlan': [1],
		'Chapultepec': [1],
		'Sevilla': [1],
		'Insurgentes': [1],
		'Cuauhtemoc': [1],
		'Balderas': [1, 3],
		'Salto del Agua': [1, 8],
		'Isabel La Catolica': [1, 2],
		'Pino Suarez': [1, 2],
		'Merced': [1],
		'Candelaria': [4],
		'San Lazaro': [1, 11],
		'Moctezuma': [1],
		'Balbuena': [1],
		'Boulevard Puerto Aereo': [1],
		'Gomez Farias': [1],
		'Zaragoza': [1],
		'Pantitlan': [1,5,9,10],
		'Cuatro Caminos': [2],
		'Tacuba': [2, 7],
		'Cuitlahuac': [2],
		'Popotla': [2],
		'Colegio Militar': [2],
		'Normal': [2],
		'San Cosme': [2],
		'Revolucion': [2],
		'Hidalgo': [2, 3],
		'Bellas Artes': [2, 8],
		'Allende': [2],
		'Zocalo': [2],
		'San Antonio Abad': [2],
		'Chabacano': [2, 8, 9],
		'Viaducto': [2],
		'Xola': [2],
		'Villa de Cortes': [2],
		'Nativitas': [2],
		'Portales': [2],
		'Ermita': [2, 12],
		'General Anaya': [2],
		'Tasqueña': [2],
		'Indios Verdes': [3],
		'Deportivo 18 de Marzo': [3, 6],
		'Potrero': [3],
		'La Raza': [3, 5],
		'Tlatelolco': [3],
		'Guerrero': [3, 11],
		'Juarez': [3],
		'Niños Heroes': [3],
		'Hospital General': [3],
		'Centro Medico': [3, 9],
		'Etiopia': [3],
		'Eugenia': [3],
		'Division del Norte': [3],
		'Zapata': [3, 12],
		'Coyoacan': [3],
		'Viveros': [3],
		'Miguel Angel de Quevedo': [3],
		'Copilco': [3],
		'Universidad': [3],
		'Martin Carrera': [4, 6],
		'Talisman': [4],
		'Bondojito': [4],
		'Consulado': [4, 5],
		'Canal del Norte': [4],
		'Morelos': [4, 11],
		'Fray Servando': [4],
		'Jamaica': [4, 9],
		'Santa Anita': [4],
		'Politecnico': [5],
		'Instituto del Petroleo': [5, 6],
		'Autobuses del Norte': [5],
		'Misterios': [5],
		'Valle Gomez': [5],
		'Eduardo Molina': [5],
		'Aragon': [5],
		'Ocenia': [5, 11],
		'Terminal Aerea': [5],
		'Hangares': [5],
		'El Rosario': [6, 7],
		'Tezozomoc': [6],
		'Azcapotzalco': [6],
		'Ferreria': [6],
		'Norte 45': [6],
		'Lindavista': [6],
		'La Villa-Basilica': [6],
		'Aquiles Serdan': [7],
		'Camarones': [7],
		'Refineria': [7],
		'San Joaquin': [7],
		'Polanco': [7],
		'Auditorio': [7],
		'Constituyentes': [7],
		'San Pedro de los Pinos': [7],
		'San Antonio': [7],
		'Mixcoac': [7, 12],
		'Barranca del Muerto': [7],
		'Garibaldi': [8, 11],
		'San Juan de Letran': [8],
		'Doctores': [8],
		'Obrera': [8],
		'La Viga': [8],
		'Coyuya': [8],
		'Iztacalco': [8],
		'Apatlaco': [8],
		'Aculco': [8],
		'Escuadron 201': [8],
		'Atlalilco': [8, 12],
		'Iztapalapa': [8],
		'Cerro de la Estrella': [8],
		'UAM-I': [8],
		'Constitucion de 1917': [8],
		'Patriotismo': [9],
		'Chilpancingo': [9],
		'Lazaro Cardenas': [9],
		'Mixiuhca': [9],
		'Velodromo': [9],
		'Ciudad Deportiva': [9],
		'Puebla': [9],
		'Agricola Oriental': [10],
		'Canal de San Juan': [10],
		'Tepalcates': [10],
		'Guelatao': [10],
		'Peñon Viejo': [10],
		'Acatitla': [10],
		'Santa Martha': [10],
		'Los Reyes': [10],
		'La Paz': [10],
		'Buenavista:': [11],
		'Lagunilla': [11],
		'Tepito': [11],
		'Flores Magon': [11],
		'Romero Rubio': [11],
		'Deportivo Oceania': [11],
		'Bosque de Aragon': [11],
		'Villa de Aragon': [11],
		'Nezahualcoyotl': [11],
		'Impulsora': [11],
		'Rio de los Remedios': [11],
		'Muzquiz': [11],
		'Ecatepec': [11],
		'Olimpica': [11],
		'Plaza Aragon': [11],
		'Ciudad Azteca': [11],
		'Insurgentes Sur': [12],
		'Hospital 20 de Noviembre': [12],
		'Parque de los Venados': [12],
		'Eje Central': [12],
		'Mexicaltzingo': [12],
		'Culhuacan': [12],
		'San Andres Tomatlan': [12],
		'Lomas Estrella': [12],
		'Calle 11': [12],
		'Periferico Oriente': [12],
		'Tezonco': [12],
		'Olivos': [12],
		'Nopalera': [12],
		'Zapotitlan': [12],
		'Tlaltengo': [12],
		'Tlahuac': [12]
		}

	return estaciones[e]
