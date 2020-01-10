def conteo_regresivo(numero):
	if(numero>0):
		print(numero)
		numero-=1
		conteo_regresivo(numero)
	else:
		print('Bang!')
		print('Termino la funcion ', numero)
n = int(input('En que numero quieres que empiece: '))
conteo_regresivo(n)

