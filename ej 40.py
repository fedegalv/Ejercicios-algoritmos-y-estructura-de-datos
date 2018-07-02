def SepararFecha(fecha, dia, mes, anio):
														  	   #01234567
	anio= fecha[0:4]
	mes= fecha[4:6]
	dia= fecha[6:8]
	print("El anio: ",anio)
	print("El mes: ",mes)
	print("El dia es: ",dia)

dia=mes=anio=0
fecha= input("Ingrese la fecha en cadena sin separacion(aaaammdd): ")
SepararFecha(fecha, dia, mes, anio)