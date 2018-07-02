from datetime import datetime

def unificarFecha(dias ,mes, anio):
	fecha=[anio,mes,dias]
	#print datetime.strptime(fecha, "%Y-%m-%d").strftime("%Y-%m-%d")
	print("%s/%s/%s" %(anio, mes, dias))

dias=input("Ingrese el dia: ")
mes= input("Ingrese el mes: ")
anio= input("Ingrese el anio: ")
unificarFecha(dias,mes, anio)