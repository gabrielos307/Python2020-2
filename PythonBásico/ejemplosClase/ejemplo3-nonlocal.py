var = 2
def funcion1():
	var = 'Hola'
	print("Estoy en la funcion 1: ",var)
	def funcion2():
		nonlocal var
		print("Estoy en la funcion 2: ",var)
	funcion2()
	print("Soy un error")
	return var
recibido = funcion1()
print("Valor recibido: ",recibido)
print("Estoy en el programa principal: ",var)