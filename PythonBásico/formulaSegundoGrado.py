#Calculo de formula general de 2do grado
import math
a = float(input("Dame el valor de 'a'"))
b = float(input("Dame el valor de 'b'"))
c = float(input("Dame el valor de 'c'"))
intRaiz = (b**2)-(4*a*c)
if(intRaiz > 0):
	raiz = math.sqrt(intRaiz)
	x1=(-b+raiz)/(2*a)
	x2=(-b-raiz)/(2*a)
	print('El valor de x1 es: ',x1)
	print('El valor de x2 es: ',x2)
elif(intRaiz<0):
	x1_entera= (-b)/(2*a)
	x1_imaginaria = (math.sqrt(intRaiz*(-1)))/(2*a)
	print('El valor de x1 es:{0}+{1}i '.format(x1_entera,x1_imaginaria))

