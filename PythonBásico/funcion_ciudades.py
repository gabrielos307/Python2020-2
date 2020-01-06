def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento
			#yield from subElemento
ciudades_devueltas = devuelve_ciudades("CDMX","Puebla","Queretaro","Guanajueto")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))