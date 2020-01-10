var = 2
def funcion1():
	global var
	var = 'Hola'
	print("Estoy en la funcion 1: ",var)
	def funcion2():
		var = 4
		print("Estoy en la funcion 2: ",var)
	funcion2()
	return var
recibido = funcion1()
print("Valor recibido: ",recibido)
print("Estoy en el programa principal: ",var)