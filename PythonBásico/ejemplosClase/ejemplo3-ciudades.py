def devuelve_ciudades(*ciudades):
	#*ciudades nos permite ingresar argumentos
	#tantos como nosotros querramos
	#print(type(ciudades))
	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento
ciudades = devuelve_ciudades("CDMX","Puebla", "Toluca")
print(next(ciudades))
print(next(ciudades))