
trigger=False

recaudacion_vuelo=[]
asiento_libre=[]
asiento_ocupado=[]
vuelos=[]
destinos=[]
pasaportes_importe={}

cont_vuelos_completos= 0
total_mes= 0
vuelo_mayor= 0
vuelo_mensual= int(input("Ingrese la cantidad de vuelos al exterior de este mes: "))
for i in range (0, vuelo_mensual):

	total_vuelo=0
	cont_pasajero= 0

	print("VUELO NUMERO ",i+1)
	nro_vuelo= int(input("\n Ingrese numero de vuelo: "))
	destino= input("Ingrese destino del vuelo: ")
	vuelos.append(nro_vuelo)
	destinos.append(destino)

	cantidad_asientos= int(input("Ingrese la cantidad de asientos en el vuelo: "))

	while trigger == False:
		print("\nINFORMACION DE PASAJEROS")
		numero_pasaporte= int(input("Ingrese numero de pasaporte: "))
		if numero_pasaporte == 0 or cont_pasajero == cantidad_asientos:
			trigger == False
			break;

		importe=int(input("Ingrese el importe que abono por el pasaje (dolares): "))
		total_vuelo= total_vuelo + importe
		cont_pasajero+= 1

		pasaportes_importe[numero_pasaporte]=importe



	asientos_ocupados_vuelo= (cont_pasajero*100)/ cantidad_asientos
	asiento_libre_vuelo= ((cantidad_asientos - cont_pasajero)*100)/ cantidad_asientos

	asiento_libre.append(asiento_libre_vuelo)
	asiento_ocupado.append(asientos_ocupados_vuelo)
	recaudacion_vuelo.append(total_vuelo)
	total_mes=total_mes + total_vuelo

	if total_vuelo > vuelo_mayor:
		vuelo_mayor=total_vuelo
		vuelo_mas_recaudo= nro_vuelo


	if cont_pasajero == cantidad_asientos:
		cont_vuelos_completos+= 1


for i in range (0, vuelo_mensual):
	print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
	print("\nNro. de vuelo: %d , Destino : %s " %(vuelos[i], destinos[i]))
	print("Nro. de Pasaporte               Importe en u$s")
	for key in pasaportes_importe:
		print("%d                              %d" %(key,pasaportes_importe[key] ))
	print("Total recaudado del vuelo: $", recaudacion_vuelo[i])
	print("Porcentaje de asientos libres del vuelo: %", asiento_libre[i])
	print("Porcentaje de asientos ocupados del vuelo: %", asiento_ocupado[i])
	


print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

print("\nTotal recaudado del mes: $",total_mes)
print("Cantidad de veces que se dieron vuelos completos: ",cont_vuelos_completos)
print("El numero del vuelo que mas recaudo: ",vuelo_mas_recaudo)


















"""print(vuelos_destinos)
print(numero_pasaporte)
print(asiento_ocupado)
print(asiento_libre)
print(total_mes)"""












