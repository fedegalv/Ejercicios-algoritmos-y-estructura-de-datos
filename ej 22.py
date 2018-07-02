fin=False
nombres_y_fechas={}
cont=0
import datetime
while fin == False:
	nombre=input("Ingrese nombre: ")
	if nombre == "fin":
		fin=True
	else:
		nombres_y_fechas[nombre]=0
		f= input("Ingrese fecha de nacimiento formato (ddmmaaaa: ")
		fecha= datetime.datetime.strptime(f, '%d%m%Y')
		nombres_y_fechas[nombre]= fecha
		cont+=1
		#print (nombres_y_fechas)

mayor_edad=0
menos_edad=0
cont=0 
"""for i in nombres_y_fechas:
	if cont == 0:
		mayor_edad= nombres_y_fechas
		menos_edad= nombres_y_fechas.value()
		nombremayor= nombres_y_fechas.keys()
		nombremenor= nombres_y_fechas.keys()


	elif cont > 0:
		if nombres_y_fechas[i] < mayor_edad:
			mayor_edad=nombres_y_fechas[i]
			nombremayor= nombres_y_fechas.keys()

		elif nombres_y_fechas[i] > menos_edad:
			menos_edad= nombres_y_fechas[i]
			nombremenor= nombres_y_fechas.keys()

	cont+=1

print("El nombre de la persona mas vieja es: "+nombremayor+" con "+mayor_edad+" anios")
print("El nombre de la persona mas joven es: "+ nombremenor+" con"+menos_edad+" anios")
"""
mayor_edad= nombres_y_fechas
print(mayor_edad)






