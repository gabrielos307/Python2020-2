var = 2
def funcion1():
	global var #Es la misma variable del programa
	print('Estoy en la funcion 1: ',var)
	def funcion2():
		var = 4 #Es una variable distinta al del programa principal
		print('Estoy en la funcion 2: ',var)
	#funcion2()
	return var
recibido = funcion1()
print('El valor recibido es: ',recibido)
print('Var del programa principal: ',var)
