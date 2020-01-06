def generaPares(limite):
	lista = []
	for i in range(1,limite):
		yield i*2
devuelve = generaPares(10)
"""
for i in devuelve:
	print(i)
"""
print(next(devuelve))
print('Continua...')
print(next(devuelve))