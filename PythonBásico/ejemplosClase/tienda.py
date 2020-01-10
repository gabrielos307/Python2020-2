lista_art=[]
montoTotal = 0
while True:
	print("****Tienda de ropa Doña conchita****")
	print("1) Jeans $350")
	print("2) Blusa $150")
	print("3) Zapatos $250")
	print("4) Camisa $350")
	print("5) Monto total")
	print("6) Salir")

	opcion = int(input("Elige opcion: "))

	if opcion == 1:
		lista_art.append("Jeans")
		montoTotal = montoTotal +350
	elif opcion == 2:
		lista_art.append("Blusa")
		montoTotal = montoTotal + 150
	elif opcion == 3:
		lista_art.append("Zapatos")
		montoTotal = montoTotal + 250
	elif opcion == 4:
		lista_art.append("Camisa")
		montoTotal = montoTotal + 350
	elif opcion == 5:
		print("El monto total de la cuenta es: "
			, montoTotal)
		if montoTotal>1000:
			descuento = montoTotal * 0.10
			total = montoTotal - descuento
			print("Se aplico un descuento y el monto es"
				,total)
		for i in lista_art:
			print(i)
	elif opcion == 6:
		break
print("Vuelve pronto")