def generaPares(limite):
	lista = []
	for i in range(0,limite):
		yield i*2 
#Cada vez que mande a llamar mi generador,
#va iterar el for yy me va regresar un valor
devuelve = generaPares(10)
#Next sirve para tomar el siguiente valor de
#un generador

"""
print(next(devuelve))
print('Aqui puede haber más código')
print(next(devuelve))
print(next(devuelve))
print(next(devuelve)) 
"""
for i in devuelve:
	print(i)


