from Abonos import *

#print(Abonos.plan_e.costo)
trigger= False
maniana_nombres=[]
maniana_direccion=[]
maniana_minutos_libres=[]
maniana_excedido=[]
maniana_total=[]

tarde_nombres=tarde_direccion=tarde_minutos_libres=tarde_excedido=tarde_total= []
noche_nombres= noche_direccion= noche_minutos_libres= noche_excedido= noche_total= []

while trigger == False:
	cont=0
	cel_0= False
	print("TURNO: Maniana")

	while cel_0 == False:
		numcel= int(input("\nIngrese numero de celular: "))
		if numcel == 0:
			cel_0= True
			break

		nombre= input("Ingrese nombre del abonado: ")
		direccion= input("Ingrese direccion del abonado: ")
		tiempo_utilizado= input("Ingrese tiempo utilizado en formato (hhmm): ")
		tipo_abono= input("Ingrese tipo de abono: ")

		total_min=toMin(tiempo_utilizado)
		#print(total_min)
		min_excedidos, total_mas_iva, min_libres = MinExc_e_IVA(tipo_abono, total_min)
		#print(min_excedidos)
		#print(total_mas_iva)
		if min_excedidos < 0:
			min_excedidos= "Ninguno"
		maniana_nombres.append(nombre)
		maniana_direccion.append(direccion)
		maniana_minutos_libres.append(min_libres)
		maniana_excedido.append(min_excedidos)
		maniana_total.append(total_mas_iva)
		cont+=1
	
	print("Turno: Maniana\n")
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("Nombre Abonado", "Direccion", "Minutos Libres" ,"Minutos Excedidos", "Monto Total a Abonar"))
	for x in range(0,cont):

		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(maniana_nombres[x], maniana_direccion[x], maniana_minutos_libres[x], maniana_excedido[x], maniana_total[x]))







	print("\nTurno: Tarde\n")
	cont=0
	cel_0= False
	while cel_0 == False:
		numcel= int(input("\nIngrese numero de celular: "))
		if numcel == 0:
			cel_0= True
			break

		nombre= input("Ingrese nombre del abonado: ")
		direccion= input("Ingrese direccion del abonado: ")
		tiempo_utilizado= input("Ingrese tiempo utilizado en formato (hhmm): ")
		tipo_abono= input("Ingrese tipo de abono: ")

		total_min=toMin(tiempo_utilizado)
		#print(total_min)
		min_excedidos, total_mas_iva, min_libres = MinExc_e_IVA(tipo_abono, total_min)
		#print(min_excedidos)
		#print(total_mas_iva)
		if min_excedidos < 0:
			min_excedidos= "Ninguno"
		tarde_nombres.append(nombre)
		tarde_direccion.append(direccion)
		tarde_minutos_libres.append(min_libres)
		tarde_excedido.append(min_excedidos)
		tarde_total.append(total_mas_iva)
		cont+=1

	print("\nTurno: Tarde\n")
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("Nombre Abonado", "Direccion", "Minutos Libres" ,"Minutos Excedidos", "Monto Total a Abonar"))
	for x in range(0,cont):

		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(tarde_nombres[x], tarde_direccion[x], tarde_minutos_libres[x], tarde_excedido[x], tarde_total[x]))






		

	print("\nTurno Noche\n")
	cont=0
	cel_0= False
	while cel_0 == False:
		numcel= int(input("\nIngrese numero de celular: "))
		if numcel == 0:
			cel_0= True
			break

		nombre= input("Ingrese nombre del abonado: ")
		direccion= input("Ingrese direccion del abonado: ")
		tiempo_utilizado= input("Ingrese tiempo utilizado en formato (hhmm): ")
		tipo_abono= input("Ingrese tipo de abono: ")

		total_min=toMin(tiempo_utilizado)
		#print(total_min)
		min_excedidos, total_mas_iva, min_libres = MinExc_e_IVA(tipo_abono, total_min)
		#print(min_excedidos)
		#print(total_mas_iva)
		if min_excedidos < 0:
			min_excedidos= "Ninguno"
		noche_nombres.append(nombre)
		noche_direccion.append(direccion)
		noche_minutos_libres.append(min_libres)
		noche_excedido.append(min_excedidos)
		noche_total.append(total_mas_iva)
		cont+=1

	print("\nTurno: Noche\n")
	print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format("Nombre Abonado", "Direccion", "Minutos Libres" ,"Minutos Excedidos", "Monto Total a Abonar"))
	for x in range(0,cont):

		print("{0:<20} {1:<20} {2:<20} {3:<20} {4:<20}".format(noche_nombres[x], noche_direccion[x], noche_minutos_libres[x], noche_excedido[x], noche_total[x]))

	trigger = True







