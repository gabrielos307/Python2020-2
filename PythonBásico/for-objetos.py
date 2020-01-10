#Programa con for que recorra 4 objetos

cadena ="Clase de python grupo 2"
lista = [1,2,3,4,5,6,7,8]
tupla = (1,2,3,4)
diccionario = {1:"uno",2:"dos",3:"tres"}

#Imprime la cadena
for i in cadena:
	print(i)
print()
#Imprime tupla 
for i in tupla:
	print(i)
print()
#Imprime lista
for i in lista:
	print(i)
print()
#Imprime diccionario
print("Empieza diccionario")
for i in diccionario:
	print(i)
print()
#Imprime las llaves del diccionario
claves = diccionario.keys()
for i in claves:
	print(i)
print()
#Imprime valores del diccionario
valores = diccionario.values()
for i in valores:
	print(i)

print()
#Imprime clave-valor
coleccion = diccionario.items()
for i in coleccion:
	print(i)