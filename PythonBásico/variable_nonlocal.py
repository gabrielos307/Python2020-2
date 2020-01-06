var = 2
def funcion1():
	var = 4 
	print('Estoy en la funcion 1: ',var)
	def funcion2():
		nonlocal var
		#var = 5
		print('Estoy en la funcion 2: ',var)
	funcion2()
	return var
recibido = funcion1()
print('El valor recibido es: ',recibido)
print('Var del programa principal: ',var)