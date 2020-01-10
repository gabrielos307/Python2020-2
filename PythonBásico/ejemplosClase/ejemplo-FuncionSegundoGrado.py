

import math #Importando la biblioteca math
def raizReal(a,b,c):
	intRaiz = (b**2)-(4*a*c)
	if(intRaiz>=0 and intRaiz >1000):
		raiz = math.sqrt(intRaiz)
		x1 = (-b+raiz)/(2*a)
		x2 = (-b-raiz)/(2*a)
		print('El valor de x1 es: ',round(x1,3))
		print('El valor de x2 es: ',round(x2,3))
	else:
		x1_real = (-b)/(2*a)
		x1_imaginaria = (math.sqrt(intRaiz*(-1)))/(2*a)
		print('El valor de x1 es:{}+{}i'.format(x1_real,round(x1_imaginaria,2)))
		print('El valor de x2 es:{}-{}i'.format(x1_real,round(x1_imaginaria,2)))
a = float(input('Dame el valor de "a": '))
b = float(input('Dame el valor de "b": '))
c = float(input('Dame el valor de "c": '))
raizReal(a,b,c)

