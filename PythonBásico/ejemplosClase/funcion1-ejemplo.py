numero1 = int(input("Dame un numero: "))
numero2 = int(input("Dame un numero: "))
def nombre_funcion(a,b):
	print("Hola soy una funcion")
	resultado = a + b
	#return resultado

regresa = nombre_funcion(numero1,numero2)
print("El resultado es: ",regresa)