def generaPares(limite):
	lista = []
	for i in range(1,limite):
		lista.append(i*2)
	return lista
print(generaPares(10))