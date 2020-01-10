def Factorial(numero):
	if(numero>1):
		numero = numero * Factorial(numero-1)
	return numero
n = int(input('Dame un numero: '))
print("El Factorial de {} es {}".format(n,Factorial(n)))