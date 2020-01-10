import math
"""
Ejercicio:
Hacer una calculadora la cual pida dos números 
pida que operacion queremos hacer y pida nos numeros 
y nos muestre el resultado
"""
def pedirNumero():
	for i in range(0,2):
		a = int(input('Dame un numero: '))
		yield a
	
def suma(x,y):
	resultado = x + y
	return resultado
def resta(x,y):
	resultado = x - y
	return resultado
def multiplicar(x,y):
	resultado = x * y
	return resultado
def division(x,y):
	resultado = x / y
	return resultado
def raiz_cuadrada(x):
	resultado = math.sqrt(x)
	return resultado
def potencia(x,y):
	resultado = x**y
	return resultado


while True: 
	print('###########################')
	print('Soy una calculadora')
	print('1- Sumar')
	print('2- Restar')
	print('3- Multiplicar')
	print('4- Dividir')
	print('5- Potencia')
	print('6- Raiz cuadrada')
	print('7- Salir')
	opcion = int(input('Elige una opcion: '))
	if(opcion == 1):
		a = next(pedirNumero())
		b = next(pedirNumero())
		resultado = suma(a,b)
		print('El resultado es: ',resultado)
	elif(opcion == 2):
		a = pedirNumero()
		b = pedirNumero()
		resultado = resta(a,b)
		print('El resultado es: ',resultado)
	elif(opcion == 3):
		a = pedirNumero()
		b = pedirNumero()
		resultado = multiplicar(a,b)
		print('El resultado es: ',resultado)
	elif(opcion == 4):
		a = pedirNumero()
		b = pedirNumero()
		resultado = division(a,b)
		print('El resultado es: ',resultado)
	elif(opcion == 5):
		a = pedirNumero()
		b = pedirNumero()
		resultado = potencia(a,b)
		print('El resultado es: ',resultado)
	elif(opcion == 6):
		a = pedirNumero()
		resultado = raiz_cuadrada(a)
		print('El resultado es: ',resultado)
	elif(opcion == 7):
		break
print('Termino el programa')


