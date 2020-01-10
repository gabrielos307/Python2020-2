def pedirNumero():
	for i in range(0,2):
		a = int(input('Dame un numero: '))
		yield a
def raiz(a):
	if a >=0:
		resultado = math.sqrt(a)
		
		return resultado
	else:
		print('El valor es negativo :C')
while True:
	print('######Calculadora######')
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
		a = next(pedirNumero())
		b = next(pedirNumero())
		resultado = resta(a,b)
		print('El resultado es: ',resultado)
	elif(opcion == 7):
		break
print('Termino la calculadora')