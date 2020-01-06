def soy_una_funcion():
	print('Hola amigos soy una funcion')

#Solamente se va ejecutar cuando nosotros la mandemos a llamar
soy_una_funcion()

def soy_otra_funcion(valor):
	print('Soy otra funcion')
	print('El valor que recibi es: ',valor)

print(soy_otra_funcion(4))

def funcion_regresa(valor):
	print('Soy la funcion que regresa')
	a = valor + 5
	return a
obtener = funcion_regresa(5)
print(obtener)
print(funcion_regresa(5))




