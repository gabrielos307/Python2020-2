'''
print('Va entrar una funcion')

def soy_una_funcion(): #para que se den cuenta que pueden nombrarla
	print('Entro a la funcion')
	a = 2
	b = 3
	c = a + b
	print(c)

soy_una_funcion()
print('Soy otra vez el main')
'''
#Validar de que entra a una funcion
valida = False
def funcion(valida):
	valida = True
	print(valida)
	return valida

funcion(valida)
print(valida)

if(valida == False):
	print('No entro la funcion')
else:
	print('Entro la funcion')
