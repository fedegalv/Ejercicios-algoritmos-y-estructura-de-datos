def DevolverBilletes(dinero):
	lista_billetes=[100,50,20,10,5,2,1]
	cantidad_billetes_usar=[]
	#print(lista_billetes)
	for i in range (0,7):
		if i == 0:
			cociente= dinero // lista_billetes[i]
			resto= dinero % lista_billetes[i]
			
			cantidad_billetes_usar.insert(i,cociente)
			dinero= resto

		if dinero != 0 and i < 7 and i > 0:
			cociente= dinero // lista_billetes[i]
			resto= dinero % lista_billetes[i]

			cantidad_billetes_usar.insert(i,cociente)
			dinero= resto
		aux=len(cantidad_billetes_usar)



	print("La cantidad de billetes a usar es: ")
	for i in range(0,aux):
		print("%d de $%d" %(cantidad_billetes_usar[i], lista_billetes[i]))


		


	#print(dinero)
	#print(cantidad_billetes_usar)

dinero=int(input("Ingrese monto a calcular: "))

DevolverBilletes(dinero)